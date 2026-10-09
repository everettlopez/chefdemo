from sqlmodel import Session, select

from app.models.item import Item
from app.schemas.item import ItemCreate


def get_items(session: Session) -> list[Item]:
    return list(session.exec(select(Item)).all())


def create_item(session: Session, item_data: ItemCreate) -> Item:
    item = Item.model_validate(item_data)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
