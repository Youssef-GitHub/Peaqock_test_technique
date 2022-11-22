from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from config import db, schema
from controllers import transaction, compte

router = APIRouter(
    prefix = '/transaction',
    tags = ['Transactions']
)

@router.get('/get', response_model=List[schema.TransactionOutput])
def getTransactions(db: Session = Depends(db.get_db)):
    return transaction.getTransactions(db)


@router.get('/get/{id}', response_model=schema.TransactionOutput)
def getTransaction(id: int, db: Session = Depends(db.get_db)):
    return transaction.getTransaction(id, db)


@router.post('/add', status_code = status.HTTP_201_CREATED,)
def addTransaction(transaction_req: schema.TransactionOutput, db: Session = Depends(db.get_db)):
    return transaction.addTransaction(transaction_req, db)


@router.put('/put/{id}', status_code = status.HTTP_202_ACCEPTED,)
def putCompte(id: int, compte_req: schema.ClientPut, db: Session = Depends(db.get_db)):
    return compte.putCompte(id, compte_req, db)


@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT,)
def deleteTransaction(id: int, db: Session = Depends(db.get_db)):
    return transaction.deleteTransaction(id, db)