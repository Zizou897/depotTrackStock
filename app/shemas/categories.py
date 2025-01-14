from sqlmodel import Field, SQLModel, Relationship



class CategoryBase(SQLModel):
    nom: str = Field(index=True)
    description: str = Field(index=True)
    parent_id: int | None = Field(default=None, index=True)
    



class CategoryResponse(CategoryBase):
    id: int | None =  Field(default=None, primary_key=True)


class CategoryCreate(CategoryBase):
    pass