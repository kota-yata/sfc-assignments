X提案アプリ (X-suggestion)

概要
- 1行のお題から「旅行プラン / 献立・レシピ / 寄せ植え植物 / 音楽プレイリスト / その他」を推定して、Webページ風に提案を表示するシンプルなアプリです。
- Gemini API をバックエンドとして呼び出します（ダミーAPIキーでも動作できるよう、モック生成を内蔵）。

要件への対応
- 入力は1行の自然言語: 画面上部のテキスト入力に1行で入力。
- 出力はWebページのような画面: カードやタグで見やすく表示。
- 専用のウィンドウ（GUI）: 単一ページ内にタイトルバー風のヘッダーを持つ専用ウィンドウUI。

使い方
1) ローカルで静的サーバを起動
   - file:// 直開きだと一部ブラウザ機能やCORSが制限されることがあるため、簡易サーバの利用を推奨します。
   - 例: Python
     - Python 3: `python -m http.server 5173`
     - ブラウザで `http://localhost:5173/` にアクセス

2) アプリを開く
   - `index.html` にアクセスすると、ウィンドウ風UIが表示されます。

3) 生成の方法を選択
   - 右側の「API設定」を開き、以下を設定できます。
     - Gemini API Key: `AIza...` を入力すると API モードに切替（CORSやネットワーク制限のある環境では失敗することがあります）。
     - 「モックで生成」にチェック: ローカルの疑似応答（オフラインでも動作）。
   - 設定は localStorage に保存されます。クリアする場合は「設定を消去」。

4) お題を入力して「生成する」
   - 例:
     - `3万円で2泊3日の京都旅行プラン`
     - `冷蔵庫: 卵, 鶏むね肉, ねぎ で献立`
     - `春で白と紫の寄せ植え`
     - `チルな夜のプレイリスト`

Gemini API
- デフォルトモデル: `gemini-1.5-flash-latest`（ドロップダウンで変更可）
- エンドポイント（自動フォールバック）:
  - まず `POST https://generativelanguage.googleapis.com/v1/models/{model}:generateContent?key=...`
  - 404 の場合は `v1beta` を再試行
- 送信メッセージには、役割説明（システム相当）とユーザのお題をまとめて渡し、`generationConfig.responseMimeType = application/json` を指定しています。
- 応答は JSON として解釈し、UI で各カテゴリ用のレイアウトにレンダリングします。

ファイル構成
- `index.html` … 画面構造
- `style.css` … スタイル（専用ウィンドウ風ヘッダーやカードUI）
- `app.js` … ロジック（Gemini呼び出し、モック、レンダリング）
- `tests/test.html` … ブラウザで開ける簡易テストランナー
- `tests/test.js` … 単体テスト（MockEngine/Renderer/escapeHtml/GeminiのJSON解析）

メモ
- このリポジトリではAPIキーを含めません（ダミー想定）。実運用時は環境変数経由のプロキシなどでキーを安全に扱ってください。
- ブラウザから直接Google APIを叩く場合、CORSの都合でサーバ側プロキシを挟む構成が安定です。

テストの実行
- 簡易サーバを起動して `http://localhost:5173/tests/test.html` を開きます。
  - Python 3: `python -m http.server 5173`
  - すべてグリーンなら「All tests passed ✅」が表示されます。
  - Gemini への実呼び出しは行いません（`fetch` をスタブして JSON 解析のみ検証）。
