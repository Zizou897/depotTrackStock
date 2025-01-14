from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from models.tables import Category

class ProduitsBase(SQLModel):
    nom: Optional[str] = Field(index=True)
    description: Optional[str] = Field(index=True)
    stock_actuel: Optional[int] | None = Field(default=None, index=True)
    seuil_alerte: Optional[int] | None = Field(default=None, index=True)
    status: Optional[str] = Field(default="actif", index=True)
    categorie_id: Optional[int] | None = Field(default=None, index=True)
    


class ProduitsResponse(ProduitsBase):
    id: int | None =  Field(default=None, primary_key=True)
    

class ProduitsCreate(ProduitsBase):
    pass
