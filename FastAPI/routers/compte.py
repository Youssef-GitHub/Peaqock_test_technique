from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from config import db, schema
from controllers import client, compte

router = APIRouter(
    prefix = '/compte',
    tags = ['Comptes']
)

@router.get('/get', response_model=List[schema.CompteOutput])
def getComptes(db: Session = Depends(db.get_db)):
    return compte.getComptes(db)


@router.get('/get/{id}', response_model=schema.CompteOutput)
def getCompte(id: int, db: Session = Depends(db.get_db)):
    return compte.getCompte(id, db)


@router.post('/add', status_code = status.HTTP_201_CREATED,)
def addCompte(compte_req: schema.CompteOutput, db: Session = Depends(db.get_db)):
    return compte.addCompte(compte_req, db)


@router.put('/put/{id}', status_code = status.HTTP_202_ACCEPTED,)
def putCompte(id: int, compte_req: schema.ClientPut, db: Session = Depends(db.get_db)):
    return compte.putCompte(id, compte_req, db)


@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT,)
def deleteCompte(id: int, db: Session = Depends(db.get_db)):
    return compte.deleteCompte(id, db)