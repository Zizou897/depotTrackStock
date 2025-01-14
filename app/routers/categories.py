from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from dependencies import get_session
from crud import categories as category_crud
from shemas.categories import CategoryCreate, CategoryResponse

router = APIRouter(tags=["Categories"])




@router.get("/api/v1/module-stock/categorie/{id}")
async def get_categorie_by_id(id : int, db: Session = Depends(get_session)):
    return await category_crud.get_categorie_by(db=db, id=id)




@router.get("/api/v1/module-stock/all-categories", response_model=list[CategoryResponse])
async def get_all_categories_(db: Session = Depends(get_session)):
    return await category_crud.get_all_categories(db=db)




@router.post("/api/v1/module-stock/categories")
async def create_categorie(category: CategoryCreate, db: Session = Depends(get_session)):
    return await category_crud.create_categorie(db=db, category=category )




@router.patch("/api/v1/module-stock/categorie/{id}")
async def update_categorie_(id: int, category: CategoryCreate, db: Session = Depends(get_session)):
    return await category_crud.update_categorie(db=db, id=id, category=category)