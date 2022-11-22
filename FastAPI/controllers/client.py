from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from config import db, model, schema

def getClients(db: Session = Depends(db.get_db)):
    clients = db.query(model.Client).all()
    return clients


def getClient(id: int, db: Session = Depends(db.get_db)):
    client = db.query(model.Client).filter(model.Client.IdPersonne == id).first()
    if not client:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Client with the id of {id} is not available'
        )
    return client


def addClient(client: schema.ClientInput, db: Session = Depends(db.get_db)):
    newClient = model.Client(
        IdPersonne = client.IdPersonne,
        IdClasse = client.IdClasse,
        IdNatureIdt = client.IdNatureIdt,
        IdPays = client.IdPays,
        NatureClient = client.NatureClient,
        Etat = client.Etat,
        IdCategorieAvoir = client.IdCategorieAvoir,
        RaisonSociale = client.RaisonSociale,
        Matricule = client.Matricule
    )
    db.add(newClient)
    db.commit()
    db.refresh(newClient)
    return newClient


def putClient(id: int, client: schema.ClientPut, db: Session = Depends(db.get_db)):
    client = db.query(model.Client).filter(model.Client.IdPersonne == id)
    if not client.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Client with the id of {id} is not available'
        )
    client.update({
        # 'IdPersonne': client.IdPersonne,
        'dClasse': client.IdClasse,
        'IdNatureIdt': client.IdNatureIdt,
        'IdPays': client.IdPays,
        'NatureClient': client.NatureClient,
        'Etat': client.Etat,
        'IdCategorieAvoir': client.IdCategorieAvoir,
        'RaisonSociale': client.RaisonSociale,
        'Matricule': client.Matricule
    })
    db.commit()
    return {'detail' : f'Client with the id of {id} is updated'}



def deleteClient(id: int, db: Session = Depends(db.get_db)):
    client = db.query(model.Client).filter(model.Client.IdPersonne == id)
    if not client.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Blog with the id of {id} is not available'
        )
    client.delete(synchronize_session = False)
    db.commit()
    return {'detail' : f'Client with the id of {id} is deleted'}