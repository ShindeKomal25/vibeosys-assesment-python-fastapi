from sqlalchemy import Column, String, Integer, BigInteger, Enum, Text, TIMESTAMP, func
from database import Base
import enum

class CategoryType(str, enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UOMType(str, enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(CategoryType), nullable=False)
    description = Column(String(250))
    product_image = Column(Text)
    sku = Column(String(100), nullable=False, unique=True)
    unit_of_measure = Column(Enum(UOMType), nullable=False)
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP, server_default=func.now())
    updated_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
