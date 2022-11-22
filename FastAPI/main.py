from fastapi import FastAPI

from routers import client, compte, transaction

app = FastAPI()

app.include_router(client.router)
app.include_router(compte.router)
app.include_router(transaction.router)