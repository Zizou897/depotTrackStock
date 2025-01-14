from sqlmodel import Field, SQLModel, Relationship




class Category(SQLModel, table=True):
    id: int | None =  Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    description: str = Field(index=True)
    parent_id: int | None = Field(default=None, index=True)
    
    #produits: list["Produits"] = Relationship(back_populates="category")
    


class Produits(SQLModel, table=True):
    id: int | None =  Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    description: str = Field(index=True)
    stock_actuel: int | None = Field(default=None, index=True)
    seuil_alerte: int | None = Field(default=None, index=True)
    status: str = Field(default="actif", index=True)
    
    categorie_id: int | None = Field(default=None, foreign_key="category.id")
    #categorie: Category | None = Relationship(back_populates="produits")






