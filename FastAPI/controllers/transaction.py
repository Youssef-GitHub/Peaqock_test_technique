from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from config import db, model, schema

def getTransactions(db: Session = Depends(db.get_db)):
    transactions = db.query(model.Transaction).all()
    return transactions


def getTransaction(id: int, db: Session = Depends(db.get_db)):
    transaction = db.query(model.Transaction).filter(model.Transaction.IdImputation == id).first()
    if not transaction:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Transaction with the id of {id} is not available'
        )
    return transaction


def addTransaction(transaction: schema.TransactionOutput, db: Session = Depends(db.get_db)):
    newTransaction = model.Transaction(
        IdImputation = transaction.IdImputation,
        IdCompteEspece = transaction.IdCompteEspece,
        Montant = transaction.Montant,
        Sens = transaction.Sens,
        DateImputation = transaction.DateImputation,
        IdDateImputation = transaction.IdDateImputation,
        IdSDBCompte = transaction.IdSDBCompte,
        DateValeur = transaction.DateValeur,
        IdDateValeur = transaction.IdDateValeur,
        Nature = transaction.Nature,
        Etat = transaction.Etat,
        DateEtat = transaction.DateEtat,
        libelle = transaction.libelle,
    )
    db.add(newTransaction)
    db.commit()
    db.refresh(newTransaction)
    return newTransaction


def putTransaction(id: int, transaction: schema.TransactionOutput, db: Session = Depends(db.get_db)):
    transaction = db.query(model.Transaction).filter(model.Transaction.IdImputation == id)
    if not transaction.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Transaction with the id of {id} is not available'
        )
    transaction.update({
        # 'IdPersonne': client.IdPersonne,
        "IdCompteEspece": transaction.IdCompteEspece,
        'Montant': transaction.Montant,
        'Sens': transaction.Sens,
        'DateImputation': transaction.DateImputation,
        'IdDateImputation': transaction.IdDateImputation,
        'IdSDBCompte': transaction.IdSDBCompte,
        'DateValeur': transaction.DateValeur,
        'IdDateValeur': transaction.IdDateValeur,
        'Nature': transaction.Nature,
        'Etat': transaction.Etat,
        'DateEtat': transaction.DateEtat,
        'libelle': transaction.libelle
    })
    db.commit()
    return {'detail' : f'Transaction with the id of {id} is updated'}



def deleteTransaction(id: int, db: Session = Depends(db.get_db)):
    transaction = db.query(model.Transaction).filter(model.Transaction.IdImputation == id)
    if not transaction.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Transaction with the id of {id} is not available'
        )
    transaction.delete(synchronize_session = False)
    db.commit()
    return {'detail' : f'Transaction with the id of {id} is deleted'}