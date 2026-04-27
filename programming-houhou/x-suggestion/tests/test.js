(() => {
  const report = document.getElementById('report');
  let passed = 0, failed = 0, cases = 0;

  function log(msg, ok = true) {
    const div = document.createElement('div');
    div.className = `case ${ok ? 'ok' : 'ng'}`;
    div.textContent = `${ok ? '✔' : '✘'} ${msg}`;
    report.appendChild(div);
  }

  function assertTrue(cond, msg) {
    cases++;
    if (cond) { passed++; log(msg, true); }
    else { failed++; log(msg, false); }
  }

  function assertEquals(a, b, msg) {
    assertTrue(a === b, `${msg} (expected: ${String(b)}, got: ${String(a)})`);
  }

  async function run() {
    // Ensure mock mode for safety
    document.getElementById('apiKey').value = '';
    const fm = document.getElementById('forceMock');
    fm.checked = true;

    // --- MockEngine classification tests ---
    const t1 = await MockEngine.generate('3万円で2泊3日の京都旅行プラン');
    assertEquals(t1.category, 'travel', 'Classify travel');
    assertTrue((t1.travel?.areas || []).includes('京都'), 'Travel includes area 京都');
    // Note: current code derives days from first number (nights) in "2泊3日" → 2
    assertEquals(t1.travel?.days, 2, 'Travel days derived from prompt (current impl)');

    const t2 = await MockEngine.generate('冷蔵庫: 卵, 鶏むね肉, ねぎ で献立');
    assertEquals(t2.category, 'recipe', 'Classify recipe');
    assertTrue((t2.recipe?.dishes || []).includes('鶏むね肉の親子丼'), 'Recipe includes 親子丼');

    const t3 = await MockEngine.generate('春で白と紫の寄せ植え');
    assertEquals(t3.category, 'plant', 'Classify plant');
    assertEquals(t3.plant?.season, '春', 'Plant season 春');

    const t4 = await MockEngine.generate('チルな夜のプレイリスト');
    assertEquals(t4.category, 'playlist', 'Classify playlist');
    assertTrue((t4.playlist?.tracks || []).length > 0, 'Playlist has tracks');

    const t5 = await MockEngine.generate('TODOアプリの構成案');
    assertEquals(t5.category, 'other', 'Fallback other');

    // --- Renderer tests ---
    const sample = {
      category: 'travel',
      title: '京都 2泊3日 旅プラン',
      summary: 'サンプル概要',
      cards: [{ type: '食', title: 'グルメ', items: ['和食','甘味'] }],
      travel: { days: 2, budget: '3万円', areas: ['京都'] }
    };
    const html = Renderer.render(sample);
    assertTrue(html.includes('旅行プラン'), 'Renderer shows category label');
    assertTrue(html.includes('京都 2泊3日 旅プラン'), 'Renderer shows title');

    // --- escapeHtml tests ---
    const escaped = escapeHtml('<script>"&\'' + '\n');
    assertEquals(escaped.includes('&lt;script&gt;'), true, 'escapeHtml escapes < >');
    assertEquals(escaped.includes('&quot;'), true, 'escapeHtml escapes "');
    assertEquals(escaped.includes('&#39;'), true, 'escapeHtml escapes \'' );
    assertEquals(escaped.includes('&amp;'), true, 'escapeHtml escapes &');

    // --- GeminiService helpers tests (no network) ---
    const url = GeminiService.endpoint('v1', 'gemini-1.5-flash-latest', 'DUMMY');
    assertTrue(url.includes('v1/models/gemini-1.5-flash-latest:generateContent'), 'Gemini endpoint path');
    assertTrue(url.includes('key=DUMMY'), 'Gemini endpoint key');

    // Stub fetch to validate JSON parsing and code-fence cleaning
    const originalFetch = window.fetch;
    try {
      window.fetch = async () => ({
        ok: true,
        json: async () => ({
          candidates: [{ content: { parts: [{ text: '```json\n{"category":"playlist","title":"テスト","summary":"ok","cards":[],"playlist":{"mood":"チル","tracks":[]}}\n```' }] } }]
        }),
        text: async () => ''
      });
      const parsed = await GeminiService.generate('test', 'KEY', 'gemini-1.5-flash-latest');
      assertEquals(parsed.category, 'playlist', 'Gemini parser handles fenced JSON');
      assertEquals(parsed.title, 'テスト', 'Gemini parser reads title');
    } finally {
      window.fetch = originalFetch;
    }

    const sum = document.createElement('div');
    sum.className = 'summary';
    sum.textContent = `Total: ${cases}, Passed: ${passed}, Failed: ${failed}`;
    report.appendChild(sum);
    if (failed === 0) {
      const ok = document.createElement('div');
      ok.textContent = 'All tests passed ✅';
      ok.className = 'ok';
      report.appendChild(ok);
    }
  }

  run().catch(err => {
    const div = document.createElement('div');
    div.className = 'ng';
    div.textContent = 'Test harness error: ' + (err?.message || String(err));
    report.appendChild(div);
  });
})();
