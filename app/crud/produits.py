from sqlmodel import Session, select
from fastapi import HTTPException


from models.tables import Produits
from shemas.produits import ProduitsCreate





async def get_all_produits(db: Session):
    produit_obj = db.exec(select(Produits)).all()
    return produit_obj


async def get_produit_by_id(db: Session, id: int):
    produit_obj =  db.get(Produits, id)
    if not produit_obj:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return produit_obj


async def create_produits(db: Session, produit: ProduitsCreate):
    db_produit = Produits.model_validate(produit)
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit


async def update_produit(db:Session, id: int, produit: ProduitsCreate):
    produit_obj = db.get(Produits, id)
    if not produit_obj:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    
    produit_data = produit.model_dump(exclude_unset=True)
    produit_obj.sqlmodel_update(produit_data)
    db.add(produit_obj)
    db.commit()
    db.refresh(produit_obj)
    return produit_obj


async def delete_produits(db: Session, id: int):
    produit_obj = db.get(Produits, id)
    if not produit_obj:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return {'ok': True}
    