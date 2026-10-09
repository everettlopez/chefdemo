from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database.session import get_session
from app.schemas.item import ItemCreate, ItemRead
from app.services.item_service import create_item, get_items

router = APIRouter(prefix="/items", tags=["items"])
SessionDependency = Annotated[Session, Depends(get_session)]


@router.get("", response_model=list[ItemRead])
def list_items(session: SessionDependency) -> list[ItemRead]:
    return get_items(session)


@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def add_item(item: ItemCreate, session: SessionDependency) -> ItemRead:
    return create_item(session, item)
