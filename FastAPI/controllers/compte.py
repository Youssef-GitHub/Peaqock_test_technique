from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from config import db, model, schema

def getComptes(db: Session = Depends(db.get_db)):
    comptes = db.query(model.Compte).all()
    return comptes


def getCompte(id: int, db: Session = Depends(db.get_db)):
    compte = db.query(model.Compte).filter(model.Compte.IdCompte == id).first()
    if not compte:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Compte with the id of {id} is not available'
        )
    return compte


def addCompte(compte: schema.CompteOutput, db: Session = Depends(db.get_db)):
    newCompte = model.Compte(
        IdCompte = compte.IdCompte,
        IdClient = compte.IdClient,
        IdDepositaire = compte.IdDepositaire,
        DateCreation = compte.DateCreation,
        Web = compte.Web,
        Etat = compte.Etat,
    )
    db.add(newCompte)
    db.commit()
    db.refresh(newCompte)
    return newCompte


def putCompte(id: int, compte: schema.CompteOutput, db: Session = Depends(db.get_db)):
    compte = db.query(model.Compte).filter(model.Compte.IdCompte == id)
    if not compte.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Client with the id of {id} is not available'
        )
    compte.update({
        # 'IdPersonne': client.IdPersonne,
        "IdClient": compte.IdClient,
        'IdDepositaire': compte.IdDepositaire,
        'DateCreation': compte.DateCreation,
        'Web': compte.Web,
        'Etat': compte.Etat,
    })
    db.commit()
    return {'detail' : f'Compte with the id of {id} is updated'}



def deleteCompte(id: int, db: Session = Depends(db.get_db)):
    compte = db.query(model.Compte).filter(model.Compte.IdCompte == id)
    if not compte.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Blog with the id of {id} is not available'
        )
    compte.delete(synchronize_session = False)
    db.commit()
    return {'detail' : f'Compte with the id of {id} is deleted'}