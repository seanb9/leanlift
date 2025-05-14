from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Size → space unit mapping
SIZE_UNITS = {
    "Small": 1,
    "Medium": 2,
    "Large": 3
}

@router.post("/shelves/")
def create_shelf(shelf: schemas.ShelfCreate, db: Session = Depends(get_db)):
    db_shelf = models.Shelf(**shelf.dict())
    db.add(db_shelf)
    db.commit()
    db.refresh(db_shelf)
    return db_shelf

@router.post("/boxes/")
def create_box(box: schemas.BoxCreate, db: Session = Depends(get_db)):
    shelf = db.query(models.Shelf).filter(models.Shelf.id == box.shelf_id).first()
    if not shelf:
        raise HTTPException(status_code=404, detail="Shelf not found")

    total_weight = box.box_count * box.weight_per_box
    size_units = SIZE_UNITS.get(box.size, 1)
    total_units = size_units * box.box_count

    if shelf.current_weight + total_weight > shelf.max_weight:
        raise HTTPException(status_code=400, detail="Shelf exceeds max weight")

    if shelf.used_units + total_units > shelf.capacity_units:
        raise HTTPException(
            status_code=400,
            detail="Not enough space in shelf for this box size and count"
        )

    new_box = models.Box(**box.dict())
    shelf.current_weight += total_weight
    shelf.used_units += total_units

    db.add(new_box)
    db.commit()
    db.refresh(new_box)
    return new_box

@router.get("/shelves/")
def get_shelves(db: Session = Depends(get_db)):
    return db.query(models.Shelf).all()

@router.get("/boxes/")
def get_boxes(db: Session = Depends(get_db)):
    return db.query(models.Box).all()


@router.delete("/boxes/{box_id}")
def delete_box(box_id: int, db: Session = Depends(get_db)):
    box = db.query(models.Box).filter(models.Box.id == box_id).first()
    if not box:
        raise HTTPException(status_code=404, detail="Box not found")

    # Revert the shelf stats
    shelf = db.query(models.Shelf).filter(models.Shelf.id == box.shelf_id).first()
    if shelf:
        size_units = SIZE_UNITS.get(box.size, 1)
        total_units = size_units * box.box_count
        total_weight = box.box_count * box.weight_per_box
        shelf.used_units = max(0, shelf.used_units - total_units)
        shelf.current_weight = max(0.0, shelf.current_weight - total_weight)

    db.delete(box)
    db.commit()
    return {"message": f"Box {box_id} deleted"}
