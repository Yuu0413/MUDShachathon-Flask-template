from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, current_user
from models import db, User, Item
from utils.database import create_item, delete_item as db_delete_item
from utils.auth import register_user, login as auth_login, logout as auth_logout

# ===================================================
# アプリの初期化
# ===================================================
app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key-here"
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    BASE_DIR, "data", "app.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "auth_page"


# ===================================================
# Flask-Login のユーザー読み込み設定
# ===================================================
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ===================================================
# ルーティング
# ===================================================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form_page():
    result = None
    if request.method == "POST":
        result = {
            "name": request.form.get("name"),
            "message": request.form.get("message"),
        }
    return render_template("form.html", result=result)


@app.route("/database", methods=["GET", "POST"])
def database_page():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description", "")
        create_item(name, description)
        flash("アイテムを追加しました！", "success")
        return redirect(url_for("database_page"))
    items = Item.query.all()
    return render_template("database.html", items=items)


@app.route("/database/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    db_delete_item(item_id)
    flash("アイテムを削除しました！", "success")
    return redirect(url_for("database_page"))


@app.route("/api")
def api_page():
    return render_template("api.html")


@app.route("/auth")
def auth_page():
    return render_template("auth.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    user, error = register_user(username, password)
    if error:
        flash(error, "error")
    else:
        flash("登録が完了しました！", "success")
    return redirect(url_for("auth_page"))


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    success, error = auth_login(username, password)
    if error:
        flash(error, "error")
    else:
        flash("ログインしました！", "success")
    return redirect(url_for("auth_page"))


@app.route("/logout")
def logout():
    auth_logout()
    flash("ログアウトしました！", "success")
    return redirect(url_for("auth_page"))


# ===================================================
# アプリの起動
# ===================================================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
