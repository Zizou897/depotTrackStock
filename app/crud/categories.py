from sqlmodel import Session, select
from fastapi import HTTPException


from models.tables import Category
from shemas.categories import CategoryCreate
import socket
import json
import zmq
from nats.aio.client import Client as NATS
import asyncio

""" 
def send_message_to_nestjs(data):
    # Connexion au service NestJS
    host = '127.0.0.1'  # Adresse IP du service NestJS
    port = 3003         # Port configuré dans NestJS

    # Créer une socket TCP
    print("###debut###")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))  # Connexion au service NestJS
        print("####niveau socket####")
        # Formatage des données en JSON
        message = json.dumps({ "cmd": "process_data", "data": data })
        print("#####niveau json#######")
        # Envoi des données au service NestJS
        client_socket.sendall(message.encode('utf-8'))
        print("#####niveausenAll#######")
        # Réception de la réponse
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Response from NestJS: {response}")

# Exemple d'utilisation
"""

async def send_message_to_nestjs(data):
    # Connexion TCP à NestJS
    print("####first commit")
    reader, writer = await asyncio.open_connection('127.0.0.1', 3000)
    
    # Préparer le message à envoyer
    print("####second commit")
    
    message = {
        'cmd': 'process_data',  # Identifiant du message
        'data': data,
    }

    # Convertir le message en format JSON
    print("####third commit")
    
    message_bytes = json.dumps(message).encode()
    print("####fourth commit")
    

    # Envoyer la longueur du message suivie du message lui-même
    writer.write(message_bytes)
    print("####fifth commit")
    
    # await writer.drain()  # Assurer l'envoi

    print(f"Sent: {message}")

    # Attendre la réponse de NestJS
    response = await reader.read(100) 
    print(response)
    # Lire jusqu'à 100 octets
    print(f"Received: {response.decode()}")

    # Fermer la connexion
    writer.close()
    await writer.wait_closed()

async def get_all_categories(db: Session):
    data = {
        'a': 3
    }
    await send_message_to_nestjs(data={})
    categorie = db.exec(select(Category)).all()
    return categorie


async def create_categorie(db: Session, category: CategoryCreate):
    db_category = Category.model_validate(category)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    data = {"message": "ok"}
    return "slut"



async def get_categorie_by(db: Session, id: int):
    category_obj = db.get(Category, id)
    if not category_obj:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    return category_obj



async def update_categorie(db: Session, id: int,category: CategoryCreate):
    category_obj = db.get(Category, id)
    if not category_obj:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    
    category_data = category.model_dump(exclude_unset=True)
    category_obj.sqlmodel_update(category_data)
    db.add(category_obj)
    db.commit()
    db.refresh(category_obj)
    return category_obj


async def delete_categorie(db:Session, id: int):
    category_obj = db.get(Category, id)
    if not category_obj:
        raise HTTPException(status_code=404, detail="Catégorie non trouvée")
    
    db.delete(category_obj)
    db.commit()
    return {'ok': True}
