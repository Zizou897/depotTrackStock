from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from dependencies import get_session
from crud import produits as produit_crud
from shemas.produits import ProduitsCreate, ProduitsResponse


router = APIRouter(tags=["Produits"])


@router.get("/api/v1/module-stock/all-produits", response_model=list[ProduitsResponse])
async def get_all_produits_(db:Session = Depends(get_session)):
    return await produit_crud.get_all_produits(db=db)



@router.get("/api/v1/module-stock/produit/{id}")
async def get_produit_by_id_(id: int, db: Session = Depends(get_session)):
    return await produit_crud.get_produit_by_id(db=db, id=id)


@router.patch("/api/v1/module-stock/produit/{id}")
async def update_produit_(id: int, produit: ProduitsCreate, db: Session = Depends(get_session)):
    return await produit_crud.update_produit(db=db, id=id, produit=produit)


@router.post("/api/v1/module-stock/produit")
async def create_produit_(produit: ProduitsCreate, db: Session = Depends(get_session)):
    return await produit_crud.create_produits(db=db, produit=produit)


