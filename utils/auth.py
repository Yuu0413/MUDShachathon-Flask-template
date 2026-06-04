from app import db, User
from flask_login import login_user, logout_user

# ===================================================
# 認証関連の操作
# ===================================================


def register_user(username, password):
    """ユーザーを新規登録する"""
    # 同じユーザー名がすでに存在する場合は登録しない
    if User.query.filter_by(username=username).first():
        return None, "このユーザー名はすでに使われています"

    # パスワードをそのまま保存（本番ではハッシュ化すること！）
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user, None


def login(username, password):
    """ログイン処理を行う"""
    user = User.query.filter_by(username=username).first()

    # ユーザーが存在しない、またはパスワードが違う場合
    if user is None or user.password != password:
        return False, "ユーザー名またはパスワードが違います"

    login_user(user)
    return True, None


def logout():
    """ログアウト処理を行う"""
    logout_user()
