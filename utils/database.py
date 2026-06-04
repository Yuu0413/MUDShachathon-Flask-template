from models import db, Item

# ===================================================
# アイテム（サンプルデータ）の操作
# ===================================================


def get_all_items():
    """全アイテムを取得する"""
    return Item.query.all()


def get_item_by_id(item_id):
    """IDでアイテムを1件取得する"""
    return Item.query.get(item_id)


def create_item(name, description=""):
    """アイテムを新規作成する"""
    item = Item(name=name, description=description)
    db.session.add(item)
    db.session.commit()
    return item


def update_item(item_id, name=None, description=None):
    """アイテムを更新する"""
    item = get_item_by_id(item_id)
    if item is None:
        return None
    if name is not None:
        item.name = name
    if description is not None:
        item.description = description
    db.session.commit()
    return item


def delete_item(item_id):
    """アイテムを削除する"""
    item = get_item_by_id(item_id)
    if item is None:
        return False
    db.session.delete(item)
    db.session.commit()
    return True
