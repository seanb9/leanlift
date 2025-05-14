from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Shelf(Base):
    __tablename__ = "shelves"
    id = Column(Integer, primary_key=True, index=True)
    lift_number = Column(Integer)
    shelf_number = Column(Integer)
    max_weight = Column(Float, default=250.0)
    current_weight = Column(Float, default=0.0)
    capacity_units = Column(Integer, default=12)
    used_units = Column(Integer, default=0)


    boxes = relationship("Box", back_populates="shelf")

class Box(Base):
    __tablename__ = "boxes"
    id = Column(Integer, primary_key=True, index=True)
    material_number = Column(String)
    batch_number = Column(String)
    size = Column(String)
    quantity = Column(Integer)
    box_count = Column(Integer)
    weight_per_box = Column(Float)
    shelf_id = Column(Integer, ForeignKey("shelves.id"))

    shelf = relationship("Shelf", back_populates="boxes")