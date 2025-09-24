from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product/list", response_model=list[schemas.ProductOut])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.get("/product/{pid}/info", response_model=schemas.ProductOut)
def product_info(pid: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id=pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add", response_model=schemas.ProductOut)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.put("/product/{pid}/update", response_model=schemas.ProductOut)
def update_product(pid: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated = crud.update_product(db, pid, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated
