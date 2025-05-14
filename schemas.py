from pydantic import BaseModel

class BoxCreate(BaseModel):
    material_number: str
    batch_number: str
    size: str
    quantity: int
    box_count: int
    weight_per_box: float
    shelf_id: int

class ShelfCreate(BaseModel):
    lift_number: int
    shelf_number: int

class Box(BaseModel):
    id: int
    material_number: str
    batch_number: str
    size: str
    quantity: int
    box_count: int
    weight_per_box: float
    shelf_id: int

    class Config:
        orm_mode = True