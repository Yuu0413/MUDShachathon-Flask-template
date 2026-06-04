# 🚀 Flask ハッカソンテンプレート

ハッカソン初参加者向けの Flask テンプレートです。
よく使う機能のサンプルをまとめています。

## 📦 含まれているサンプル

| サンプル | 説明 |
|---|---|
| 📝 フォーム | 入力フォームの作り方・データの受け取り方 |
| 🗄️ DB連携 | SQLite を使ったデータの保存・取得・削除 |
| 🌐 外部API連携 | 外部 API を叩いてデータを取得・表示する |
| 🔐 ログイン機能 | ユーザー登録・ログイン・ログアウトの実装 |

## 🛠️ 使用技術

- **Flask** - Web フレームワーク
- **Flask-SQLAlchemy** - DB 連携
- **Flask-Login** - 認証機能
- **requests** - 外部 API 連携
- **uv** - パッケージ管理

## 🚀 セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/【ユーザー名】/hackathon-flask-template.git
cd hackathon-flask-template
```

### 2. 仮想環境を作成・有効化

```bash
uv venv
source .venv/bin/activate  # Mac/Linux
```

### 3. パッケージをインストール

```bash
uv sync
```

### 4. アプリを起動

```bash
python app.py
```

ブラウザで `http://127.0.0.1:5000` を開いてください。

## 📁 ファイル構成

```
hackathon-flask-template/
│
├── static/
│   ├── css/
│   │   └── style.css        # スタイルシート
│   └── js/
│       └── main.js          # JavaScript
│
├── templates/
│   ├── base.html            # ベーステンプレート
│   ├── index.html           # トップページ
│   ├── form.html            # フォームサンプル
│   ├── database.html        # DB連携サンプル
│   ├── api.html             # 外部API連携サンプル
│   └── auth.html            # ログイン機能サンプル
│
├── utils/
│   ├── __init__.py
│   ├── database.py          # DB操作の関数
│   └── auth.py              # 認証関連の関数
│
├── data/
│   └── .gitkeep
│
├── app.py                   # Flask アプリのエントリーポイント
├── models.py                # DB モデル定義
├── pyproject.toml           # パッケージ管理
└── README.md
```

## ⚠️ 本番環境への注意点

- `SECRET_KEY` は必ず `.env` から読み込むように変更してください
- パスワードは必ずハッシュ化してください（`werkzeug.security` が便利です）
- `debug=True` は本番環境では外してください