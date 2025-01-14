from typing import Annotated
from fastapi import FastAPI, Depends, Request
from sqlmodel import Session
import requests
import asyncio 
import socket

from database import create_db_and_tables
from dependencies import get_session
from routers import (
    categories,
    produits
)


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()



async def handle_tcp_connection(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received: {message}")
        # Traitement du message reçu
        response = f"You sent me: {message}"
        writer.write(response.encode())
        await writer.drain()


async def start_tcp_server():
    server = await asyncio.start_server(handle_tcp_connection, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()


def register_service():

    response = requests.post("http://127.0.0.1:3003/discovery/register",{
        "name": "stock",
        "host": "127.0.0.1",
        "port": 3003,
        "apiKey": "",
        
    })
    

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    #register_service()
    asyncio.create_task(start_tcp_server())
    
    

@app.get("/")
def read_root():
    return {"hello world 1"}


app.include_router(categories.router)
app.include_router(produits.router)