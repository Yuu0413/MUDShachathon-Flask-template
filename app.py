from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# ===================================================
# アプリの初期化
# ===================================================
app = Flask(__name__)

# シークレットキー（セッション管理・ログイン機能に必要）
# 本番環境では .env から読み込むこと！
app.config["SECRET_KEY"] = "your-secret-key-here"

# データベースの設定（SQLite を使用）
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ===================================================
# 拡張機能の初期化
# ===================================================
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth_page"  # 未ログイン時のリダイレクト先


# ===================================================
# モデル（データベースのテーブル定義）
# ===================================================
class User(db.Model):
    """ユーザーテーブル"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Flask-Login に必要なプロパティ
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Item(db.Model):
    """サンプルデータテーブル"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))


# ===================================================
# Flask-Login のユーザー読み込み設定
# ===================================================
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ===================================================
# ルーティング（URLとページの対応）
# ===================================================
@app.route("/")
def index():
    """トップページ"""
    return render_template("index.html")


@app.route("/form")
def form_page():
    """フォームサンプルページ"""
    return render_template("form.html")


@app.route("/database")
def database_page():
    """DB連携サンプルページ"""
    items = Item.query.all()
    return render_template("database.html", items=items)


@app.route("/api")
def api_page():
    """外部API連携サンプルページ"""
    return render_template("api.html")


@app.route("/auth")
def auth_page():
    """ログイン機能サンプルページ"""
    return render_template("auth.html")


# ===================================================
# アプリの起動
# ===================================================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # テーブルが存在しない場合は自動作成
    app.run(debug=True)
