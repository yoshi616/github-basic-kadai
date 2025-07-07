ChatGPT Flaskアプリ

　OpenAIのAPIを使って、ターミナルとWebブラウザの両方でChatGPTと対話できるシンプルなチャットボットアプリです。  
　初心者のエンジニアが学習目的で開発したプロジェクトです。


ファイル構成

ファイル名・フォルダ（説明）
`chatbot.py` （ターミナルでChatGPTと対話するスクリプト）
`app.py` （Flaskを使ったWebアプリ）
`templates/index.html` （WebアプリのHTMLテンプレート）
`.env` （APIキーを記述（Gitには含めない））
`.gitignore` （`.env` を除外設定）
`README.md` （このファイル）

実行方法

1. 必要なライブラリをインストール（下記のコマンドをVSCodeのターミナルで実行）
pip install openai flask python-dotenv
2. .env ファイルを作成（プロジェクトのルートディレクトリに）
3. ターミナルでpython chatbot.pyを実行
質問の入力によって、ChatGPTの応答がターミナルに表示
4. Webアプリを起動
python app.pyを実行・アクセスすると、ブラウザでチャット画面が表示される


[全体工程]の説明
1. 企画フェーズ
・課題：OpenAI社のChatGPT APIを活用したシンプルなチャットボットを開発
・機能要件（箇条書き）
ユーザーからの入力を受け取る画面
ChatGPT APIへのリクエスト送信
レスポンスの表示
・使用技術の選定
Python
Flask（Webアプリケーションフレームワーク）
HTML（ユーザーインターフェース）

2. 設計フェーズ
・システム構成図の作成
[ユーザーのブラウザ]
       ↓ ↑ （入力／応答）
   [HTML画面（index.html）]
       ↓ ↑ （フォーム送信／応答表示）
   [Flaskアプリ（app.py）]
       ↓ ↑ （関数呼び出し）
[get_chatgpt_response(prompt)]
       ↓ ↑ （APIリクエスト／応答）
[OpenAI ChatGPT API]

・開発環境のセットアップ
VS Code + GitHub Codespaces（クラウド開発環境）
python仮想環境
OpenAI APIキーの取得
.env ファイルを作成し、APIキーを環境変数として管理
python-dotenv を使って .env を読み込む
.env を .gitignore に追加し、GitHubにアップロードされないように設定

3. 開発フェーズ
・バックエンド実装 (python)
chatbot.py にて、ChatGPT APIを呼び出すスクリプトを作成
get_chatgpt_response() 関数に try-except を追加し、エラー処理を追加
Flaskアプリ（app.py）を作成し、WebフォームとAPIを連携
・フロントエンド実装（HTML）
templates/index.html にHTMLテンプレートを作成
<form method="POST"> を使って、ユーザー入力をサーバーに送信
ChatGPTの応答を画面に表示
4. テスト・デバッグフェーズ
・手動テストチェックリスト作成
[ ] 空の入力を送信したときにエラーが出ないか確認
[ ] 長文を送っても応答が返ってくるか確認
[ ] APIキーが無効なときにエラーメッセージを表示できるか確認
・デバックの手順
ls で正しいディレクトリにいるか確認
pip show flask で Flask がインストールされているか確認
python app.py でアプリを起動
VS Code の「PORTS」タブからブラウザを開き、チャット画面を確認

開発環境のセットアップ詳細
    pip install openai：OpenAIライブラリのインストール
    touch chatbot.py → code chatbot.py：Pythonファイルの作成と編集
    pip install flask：Flaskのインストール
    touch app.py → code app.py：Flaskアプリの作成
    mkdir templates → touch templates/index.html：HTMLテンプレートの作成

5. 今後、追加実施できる内容（拡張案）
・ フロントエンド
ReactやVueなどのJavaScriptフレームワークを導入し、より動的なUIを実現
    （今回は以下の理由で未採用：
      ① HTMLフォームで十分にユーザー入力を処理できる  
      ② Flaskがサーバー側でレスポンスを生成して表示しているため）
 CSSでUIを装飾（背景色・吹き出し・チャット風デザインなど）

・ API化と外部連携
 FlaskをAPIモードで構築、またはFastAPIを導入し、モバイルアプリや外部サービスと連携可能なREST APIを提供
 JSON形式のレスポンスを返すように変更し、ReactやJavaScriptから非同期通信（AJAX）でデータ取得できるようにする

・ その他の拡張
 入力履歴の保存（セッション管理やデータベース連携を行えればよい）
Heroku, AWS, GCP などへのデプロイを検討
