from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from config.db import Base

class Client(Base):
    __tablename__ = 'Clients'

    IdPersonne = Column(Integer, primary_key = True, index = True)
    IdClasse = Column(Integer)
    IdNatureIdt = Column(Integer)
    IdPays = Column(Integer)
    NatureClient = Column(String)
    Etat = Column(String)
    IdCategorieAvoir = Column(Integer)
    RaisonSociale = Column(String)
    Matricule = Column(String)

    comptes = relationship('Compte', back_populates = 'client')


class Compte(Base):
    __tablename__ = 'ComptesEspece'

    IdCompte = Column(Integer, primary_key = True, index = True)
    IdClient = Column(Integer, ForeignKey('Clients.IdPersonne'))
    IdDepositaire = Column(Integer)
    DateCreation = Column(DateTime)
    Web = Column(String)
    Etat = Column(String)

    client = relationship('Client', back_populates = 'comptes')
    transactions = relationship('Transaction', back_populates = 'compte')


class Transaction(Base):
    __tablename__ = 'ImputationsEspeces'

    IdImputation = Column(Integer, primary_key = True, index = True)
    IdCompteEspece = Column(Integer, ForeignKey('ComptesEspece.IdCompte'))
    Montant = Column(Float)
    Sens = Column(Integer)
    DateImputation = Column(DateTime)
    IdDateImputation = Column(Integer)
    IdSDBCompte = Column(Integer)
    DateValeur = Column(DateTime)
    IdDateValeur = Column(Integer)
    Nature = Column(String)
    Etat = Column(Integer)
    DateEtat = Column(DateTime)
    libelle = Column(String)

    compte = relationship('Compte', back_populates = 'transactions')