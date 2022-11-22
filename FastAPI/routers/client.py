from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from config import db, schema
from controllers import client

router = APIRouter(
    prefix = '/client',
    tags = ['Clients']
)

# , current_user: schemas.User = Depends(get_current_user)
@router.get('/get', response_model=List[schema.ClientOutput])
def getClients(db: Session = Depends(db.get_db)):
    return client.getClients(db)


@router.get('/get/{id}', response_model=schema.ClientOutput)
def getClient(id: int, db: Session = Depends(db.get_db)):
    return client.getClient(id, db)


@router.post('/add', status_code = status.HTTP_201_CREATED,)
def addClient(client_req: schema.ClientInput, db: Session = Depends(db.get_db)):
    return client.addClient(client_req, db)


@router.put('/put/{id}', status_code = status.HTTP_202_ACCEPTED,)
def putClient(id: int, client_req: schema.ClientPut, db: Session = Depends(db.get_db)):
    return client.putClient(id, client_req, db)


@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT,)
def deleteClient(id: int, db: Session = Depends(db.get_db)):
    return client.deleteClient(id, db)