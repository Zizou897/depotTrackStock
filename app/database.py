from sqlmodel import Session, SQLModel, create_engine



SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/depotT_bd"


connect_args = {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL)



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    