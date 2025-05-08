from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.models.item import Item
from app.schemas.item import Item as ItemSchema
from app.schemas.item import ItemCreate, ItemUpdate

router = APIRouter()


@router.get("/", response_model=List[ItemSchema])
def read_items(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items


@router.post("/", response_model=ItemSchema)
def create_item(
    *,
    db: Session = Depends(get_db),
    item_in: ItemCreate
):
    item = Item(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/{item_id}", response_model=ItemSchema)
def read_item(
    *,
    db: Session = Depends(get_db),
    item_id: int
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=ItemSchema)
def update_item(
    *,
    db: Session = Depends(get_db),
    item_id: int,
    item_in: ItemUpdate
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)

    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}")
def delete_item(
    *,
    db: Session = Depends(get_db),
    item_id: int
):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"ok": True}
