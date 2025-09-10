# シンプルなWeb APIの作成（Python + Flask）

## 0. 事前準備
- 「api_ping」フォルダを作成し、以下のファイルを配置
  - app.py（APIの本体）
  - requirements.txt（必要なパッケージリスト）
  - README.md（この説明書）

## 1. 必要なパッケージのインストール
- ターミナルで以下を実行
pip install -r requirements.txt
※requirements.txtには「flask」と記載

## 2. サーバーの起動
- ターミナルで以下を実行
python app.py
- サーバーが起動すると、`http://127.0.0.1:5000/` でアクセス可能

## 3. APIのテスト
- 別のターミナルを開いて、以下を実行
curl http://127.0.0.1:5000/api/ping
- 期待される応答
{"pong": true}
