// X-suggestion App (Gemini + mock fallback)

const UI = {
  input: document.getElementById('promptInput'),
  btn: document.getElementById('generateBtn'),
  clearBtn: document.getElementById('clearBtn'),
  result: document.getElementById('result'),
  apiStatus: document.getElementById('apiStatus'),
  apiKey: document.getElementById('apiKey'),
  modelSelect: document.getElementById('modelSelect'),
  forceMock: document.getElementById('forceMock'),
  saveSettings: document.getElementById('saveSettings'),
  clearSettings: document.getElementById('clearSettings'),
};

const SETTINGS_KEY = 'x_suggestion_settings_v1';

function loadSettings() {
  try {
    const raw = localStorage.getItem(SETTINGS_KEY);
    if (!raw) return {};
    return JSON.parse(raw) || {};
  } catch {
    return {};
  }
}

function saveSettings(settings) {
  localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
}

let settings = loadSettings();
UI.apiKey.value = settings.apiKey || '';
UI.modelSelect.value = settings.model || 'gemini-1.5-flash-latest';
UI.forceMock.checked = !!settings.forceMock;

function updateApiStatus() {
  const mode = UI.forceMock.checked ? 'mock' : (UI.apiKey.value ? 'gemini' : 'mock');
  const model = UI.modelSelect?.value || 'gemini-1.5-flash-latest';
  UI.apiStatus.textContent = `API: ${mode}${mode==='gemini' ? ' · '+model : ''}`;
}
updateApiStatus();

UI.saveSettings.addEventListener('click', () => {
  settings = {
    apiKey: UI.apiKey.value.trim(),
    model: UI.modelSelect.value,
    forceMock: UI.forceMock.checked,
  };
  saveSettings(settings);
  updateApiStatus();
});
UI.clearSettings.addEventListener('click', () => {
  settings = {};
  saveSettings(settings);
  UI.apiKey.value = '';
  UI.modelSelect.value = 'gemini-1.5-flash-latest';
  UI.forceMock.checked = false;
  updateApiStatus();
});

UI.clearBtn.addEventListener('click', () => {
  UI.result.innerHTML = '';
  UI.input.value = '';
  UI.input.focus();
});

UI.btn.addEventListener('click', generateSuggestion);
UI.input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    generateSuggestion();
  }
});

function setBusy(busy) {
  UI.result.setAttribute('aria-busy', busy ? 'true' : 'false');
  UI.btn.disabled = busy;
}

async function generateSuggestion() {
  const prompt = UI.input.value.trim();
  if (!prompt) {
    toast('お題を1行で入力してください');
    UI.input.focus();
    return;
  }
  setBusy(true);
  UI.result.innerHTML = renderLoading();
  try {
    const useMock = UI.forceMock.checked || !UI.apiKey.value.trim();
    const model = UI.modelSelect.value || 'gemini-1.5-flash-latest';
    const data = useMock
      ? await MockEngine.generate(prompt)
      : await GeminiService.generate(prompt, UI.apiKey.value.trim(), model);
    UI.result.innerHTML = Renderer.render(data);
  } catch (err) {
    console.error(err);
    UI.result.innerHTML = renderError(err);
  } finally {
    setBusy(false);
  }
}

function renderLoading() {
  return `<div class="meta">生成中… 少々お待ちください。</div>`;
}

function renderError(err) {
  const msg = typeof err === 'string' ? err : (err?.message || '不明なエラー');
  return `<div class="meta" style="color: var(--danger)">エラー: ${escapeHtml(msg)}</div>`;
}

function toast(message) {
  UI.result.innerHTML = `<div class="meta">${escapeHtml(message)}</div>`;
}

const GeminiService = {
  endpoint(version, model, apiKey) {
    const base = `https://generativelanguage.googleapis.com/${version}`;
    return `${base}/models/${encodeURIComponent(model)}:generateContent?key=${encodeURIComponent(apiKey)}`;
  },
  async generate(prompt, apiKey, model) {
    const sys = buildSystemPrompt();
    const body = {
      contents: [
        { role: 'user', parts: [ { text: sys + "\n\n# User Prompt\n" + prompt } ] }
      ],
      generationConfig: {
        responseMimeType: 'application/json',
        temperature: 0.7,
      },
    };

    // Try v1 first, then v1beta for compatibility
    const versions = ['v1', 'v1beta'];
    let lastErr;
    for (const ver of versions) {
      try {
        const res = await fetch(this.endpoint(ver, model, apiKey), {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        });
        if (!res.ok) {
          const text = await res.text().catch(() => '');
          // If NOT_FOUND, try next version
          if (res.status === 404) {
            lastErr = new Error(`Gemini API failed: ${res.status} ${text}`);
            continue;
          }
          throw new Error(`Gemini API failed: ${res.status} ${text}`);
        }
        const json = await res.json();
        return parseGeminiJson(json);
      } catch (e) {
        lastErr = e;
        continue;
      }
    }
    // If both versions failed with 404 or any error
    const tip = `モデルが利用不可の可能性があります。'${model}' を 'gemini-1.5-flash-latest' に変更、または API の有効化/地域設定を確認してください。`;
    throw new Error((lastErr?.message || 'Gemini API error') + `\nHint: ${tip}`);
  }
};

function parseGeminiJson(json) {
  const candidates = json?.candidates || [];
  const parts = candidates[0]?.content?.parts || [];
  const text = parts[0]?.text || '';
  if (!text) throw new Error('空の応答');
  const cleaned = text.replace(/^```(?:json)?\n|```$/g, '');
  try {
    return JSON.parse(cleaned);
  } catch (e) {
    throw new Error('JSONの解析に失敗しました: ' + e.message);
  }
}

function buildSystemPrompt() {
  return `You are X-suggestion app (Japanese UI).\n\nGoal:\n- Given ONE-LINE natural language prompt (Japanese or English), infer the best suggestion domain and produce a compact plan as JSON.\n- Supported domains: 旅行プラン (travel), 献立・レシピ (recipe), 寄せ植え植物 (container planting), 音楽プレイリスト (playlist), その他 (other).\n- Use details in the prompt (budget, dates/days, places, available ingredients, season, flower colors, mood, etc.).\n\nOutput schema (application/json):\n{\n  "+meta": { version: "1.0" },\n  "category": "travel|recipe|plant|playlist|other",\n  "title": string,\n  "summary": string,\n  "cards": [ // small digestible cards for a web-like page\n    { "type": string, "title": string, "items": string[] }\n  ],\n  // domain-specific fields (optional)\n  "travel"?: { days?: number, budget?: string, areas?: string[], daily_plan?: string[][] },\n  "recipe"?: { meals?: string[], dishes?: string[], shopping_list?: string[] },\n  "plant"?: { season?: string, colors?: string[], plants?: string[], layout_tips?: string[] },\n  "playlist"?: { mood?: string, tracks?: { title: string, artist: string }[] }\n}\n\nConstraints:\n- Keep JSON small but useful (3-6 bullets per list).\n- Japanese text.\n- No markdown, no extra commentary. Return ONLY JSON.`;
}

const Renderer = {
  render(data) {
    try {
      const { category, title, summary, cards } = data;
      const chips = this.renderChips(category, data);
      const cardHtml = (cards || []).map(this.renderCard).join('');
      const special = this.renderSpecial(category, data);
      return `
        <div class="pill">${this.categoryLabel(category)}</div>
        <h2>${escapeHtml(title || '提案')}</h2>
        <div class="meta">${escapeHtml(summary || '')}</div>
        <div style="margin-top:10px">${chips}</div>
        ${special}
        <div class="grid" style="margin-top: 12px;">${cardHtml}</div>
      `;
    } catch (e) {
      console.error('Render error', e, data);
      return renderError(e);
    }
  },
  renderChips(category, data) {
    const chips = [];
    if (category === 'travel') {
      if (data?.travel?.budget) chips.push(this.pill(`予算: ${data.travel.budget}`));
      if (data?.travel?.days) chips.push(this.pill(`${data.travel.days}日`));
      if (data?.travel?.areas?.length) chips.push(this.pill(`場所: ${data.travel.areas.join(' / ')}`));
    } else if (category === 'recipe') {
      if (data?.recipe?.meals?.length) chips.push(this.pill(`食事: ${data.recipe.meals.join(' / ')}`));
    } else if (category === 'plant') {
      if (data?.plant?.season) chips.push(this.pill(`時期: ${data.plant.season}`));
      if (data?.plant?.colors?.length) chips.push(this.pill(`色: ${data.plant.colors.join(' & ')}`));
    } else if (category === 'playlist') {
      if (data?.playlist?.mood) chips.push(this.pill(`雰囲気: ${data.playlist.mood}`));
    }
    return chips.join('');
  },
  renderCard(card) {
    const title = escapeHtml(card.title || '');
    const items = (card.items || []).map(i => `<li>${escapeHtml(i)}</li>`).join('');
    return `<div class="card"><div class="meta" style="margin-bottom:6px;">${escapeHtml(card.type || '')}</div><div><strong>${title}</strong></div><ul class="list">${items}</ul></div>`;
  },
  renderSpecial(category, data) {
    if (category === 'playlist' && data?.playlist?.tracks?.length) {
      const tracks = data.playlist.tracks.slice(0, 12).map(t => `<li>${escapeHtml(t.title)} — <span class="meta">${escapeHtml(t.artist)}</span></li>`).join('');
      return `<div class="card" style="margin-top:10px"><div><strong>候補トラック</strong></div><ul class="list">${tracks}</ul></div>`;
    }
    if (category === 'travel' && data?.travel?.daily_plan?.length) {
      const days = data.travel.daily_plan.map((d, idx) => `<div class="card"><strong>Day ${idx+1}</strong><ul class="list">${d.map(x=>`<li>${escapeHtml(x)}</li>`).join('')}</ul></div>`).join('');
      return `<div class="grid" style="margin-top:10px">${days}</div>`;
    }
    return '';
  },
  pill(text) {
    return `<span class="pill">${escapeHtml(text)}</span>`;
  },
  categoryLabel(cat) {
    switch (cat) {
      case 'travel': return '旅行プラン';
      case 'recipe': return '献立・レシピ';
      case 'plant': return '寄せ植え植物';
      case 'playlist': return '音楽プレイリスト';
      default: return 'その他の提案';
    }
  }
};

const MockEngine = {
  async generate(prompt) {
    // Simple heuristic-based classifier
    const p = prompt.toLowerCase();
    const isTravel = /旅|旅行|trip|travel|観光/.test(prompt);
    const isRecipe = /献立|レシピ|料理|冷蔵|fridge|recipe|cook/.test(prompt);
    const isPlant = /寄せ植え|植物|プランター|花壇|植栽|plant|container/.test(prompt);
    const isPlaylist = /プレイリスト|音楽|曲|playlist|music|mood/.test(prompt);

    if (isTravel) return this.travel(prompt);
    if (isRecipe) return this.recipe(prompt);
    if (isPlant) return this.plant(prompt);
    if (isPlaylist) return this.playlist(prompt);
    // Fallback: choose by cues
    if (/円|万円|budget|泊|日/.test(prompt)) return this.travel(prompt);
    if (/,|、|卵|肉|魚|ねぎ|玉ねぎ|トマト/.test(prompt)) return this.recipe(prompt);
    if (/春|夏|秋|冬|白|紫|赤|青|黄|ピンク/.test(prompt)) return this.plant(prompt);
    if (/チル|アップテンポ|ロック|ジャズ|lofi|hip hop|pop|ambient/.test(p)) return this.playlist(prompt);
    return this.other(prompt);
  },
  extractBudgetDaysAreas(prompt) {
    const budget = (prompt.match(/([0-9]+)\s*万?円/) || [])[0] || '';
    const days = (prompt.match(/([0-9]+)泊([0-9]+)日/) || [])[0] || (prompt.match(/([0-9]+)日間?/) || [])[0] || '';
    const areas = (prompt.match(/(京都|大阪|沖縄|北海道|東京|福岡|金沢|箱根|奈良)/g) || []).slice(0,3);
    return { budget, days, areas };
  },
  travel(prompt) {
    const { budget, days, areas } = this.extractBudgetDaysAreas(prompt);
    const locs = areas.length ? areas : ['京都','奈良'];
    return {
      "+meta": { version: '1.0', mock: true },
      category: 'travel',
      title: `${locs.join('・')} ${days || '2泊3日'} 旅プラン`,
      summary: `${budget || '3万円程度'} で満足度の高い観光・食・移動を最適化`,
      travel: {
        days: /([0-9]+)/.test(days) ? Number(RegExp.$1) : 3,
        budget: budget || '約3万円',
        areas: locs,
        daily_plan: [
          ['到着 → 宿に荷物','祇園・清水寺散策','京うどんの昼食','二年坂・三年坂カフェ','先斗町で夕食'],
          ['伏見稲荷の早朝参拝','抹茶スイーツ','嵐山エリア散策','竹林・渡月橋','湯豆腐の晩ごはん'],
          ['錦市場で食べ歩き','お土産タイム','銭湯で〆','帰路']
        ]
      },
      cards: [
        { type: '移動/交通', title: 'ICカード＋徒歩中心', items: ['主要観光地はバス1日券で効率化','朝は混雑前に人気スポットへ','荷物は駅ロッカー活用'] },
        { type: '食', title: '定番と穴場をミックス', items: ['ランチは並ばない名店を狙う','夜は先斗町で鴨川の見える席','甘味は抹茶パフェで季節感'] },
        { type: '節約Tips', title: 'コスパ良く楽しむ', items: ['早割で宿予約','朝食は市場で軽めに','拝観料はセット券活用'] }
      ]
    };
  },
  recipe(prompt) {
    const ingredients = (prompt.split(/:|：/)[1] || '')
      .split(/,|、|\s/)
      .map(s => s.trim()).filter(Boolean).slice(0,6);
    const base = ingredients.length ? ingredients : ['卵','鶏むね肉','ねぎ'];
    return {
      "+meta": { version: '1.0', mock: true },
      category: 'recipe',
      title: `あるもので即席献立`,
      summary: `${base.join('・')} を活用して30分以内で作れる献立`,
      recipe: {
        meals: ['夕食'],
        dishes: ['鶏むね肉の親子丼','長ねぎの味噌汁','きゅうりの浅漬け'],
        shopping_list: ['だしパック','万能ねぎ','漬け物用の浅漬けの素']
      },
      cards: [
        { type: '主菜', title: '鶏むね肉の親子丼', items: ['鶏むね肉をそぎ切り','出汁＋醤油＋みりんで煮る','溶き卵を2回に分けて半熟に'] },
        { type: '汁物', title: '長ねぎの味噌汁', items: ['昆布＋鰹で出汁','長ねぎを斜め薄切り','最後に味噌を溶く'] },
        { type: '副菜', title: 'きゅうりの浅漬け', items: ['薄切りで塩もみ','水気を絞る','浅漬けの素で10分'] }
      ]
    };
  },
  plant(prompt) {
    const season = (prompt.match(/春|夏|秋|冬/) || ['春'])[0];
    const color = (prompt.match(/白|紫|赤|青|黄|ピンク/g) || ['白','紫']).slice(0,2);
    return {
      "+meta": { version: '1.0', mock: true },
      category: 'plant',
      title: `季節の寄せ植え (${season}・${color.join('×')})`,
      summary: `${season}らしさと ${color.join('×')} の色合わせで長持ちする寄せ植え`,
      plant: {
        season,
        colors: color,
        plants: ['ビオラ','アリッサム','ラベンダー','アイビー'],
        layout_tips: ['背の高い主役を後方に','中間を色でリズム付け','縁から垂れる葉でこなれ感']
      },
      cards: [
        { type: '配色', title: 'トーンを揃える', items: ['白は清潔感の基調','紫は引き締め役','葉色で中和'] },
        { type: '鉢・土', title: '8〜10号で深さを確保', items: ['培養土＋緩効性肥料','底石で排水','仕上げにバークチップ'] },
        { type: '手入れ', title: '花がら摘みで開花継続', items: ['週1の液肥','日当たり4時間以上','風通しを意識'] }
      ]
    };
  },
  playlist(prompt) {
    const mood = (prompt.match(/チル|アップテンポ|しっとり|爽やか|夜|朝|lofi|rock|jazz|pop|ambient/i) || ['チル'])[0];
    const tracks = [
      { title: 'Night Drive', artist: 'K. Rivers' },
      { title: 'City Lights', artist: 'M. Hikari' },
      { title: 'Soft Rain', artist: 'A. Kumo' },
      { title: 'Blue Hour', artist: 'S. Aoi' },
      { title: 'Neon Echo', artist: 'Y. Neon' },
      { title: 'Velvet Steps', artist: 'L. Velvet' },
      { title: 'Late Latte', artist: 'C. Cafe' }
    ];
    return {
      "+meta": { version: '1.0', mock: true },
      category: 'playlist',
      title: `${typeof mood === 'string' ? mood : 'チル'}な雰囲気のプレイリスト`,
      summary: '作業やリラックスに合う落ち着いた選曲',
      playlist: { mood: String(mood), tracks },
      cards: [
        { type: '方向性', title: 'テンポと質感', items: ['BPMは70-100程度','アタック弱めで柔らかい質感','ピアノ/ギター/パッド主体'] },
        { type: '流れ', title: '序盤→中盤→終盤', items: ['導入は環境音で静かに','中盤でメロディを際立たせる','終盤で余韻を残す'] },
        { type: '場面', title: '相性', items: ['夜の読書','深夜ドライブ','コーディング'] }
      ]
    };
  },
  other(prompt) {
    return {
      "+meta": { version: '1.0', mock: true },
      category: 'other',
      title: '自由なお題への提案',
      summary: '内容から要点を拾い、実行手順とヒントを提示',
      cards: [
        { type: '要点', title: 'ポイント', items: ['目的を明確化','制約条件を洗い出す','成果物の基準を定義'] },
        { type: '手順', title: '最小実行計画', items: ['タスク分解','優先度付け','検証のチェックリスト化'] },
        { type: 'リスク', title: '詰まりやすい所', items: ['情報不足','スコープ過多','スケジュール遅延'] }
      ]
    };
  }
};

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  }[c]));
}

// Initial focus for quick typing
UI.input.focus();
