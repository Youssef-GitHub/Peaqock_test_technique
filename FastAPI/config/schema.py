from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class ClientOutput(BaseModel):
    IdPersonne: int
    IdClasse: int
    IdNatureIdt: int
    IdPays: int
    NatureClient: str
    Etat: str
    IdCategorieAvoir: int
    RaisonSociale: str
    Matricule: str

    class Config():
        orm_mode = True


class ClientInput(BaseModel):
    IdPersonne: int
    IdClasse: int
    IdNatureIdt: int
    IdPays: int
    NatureClient: str
    Etat: str
    IdCategorieAvoir: int
    RaisonSociale: str
    Matricule: str

    class Config():
        orm_mode = True


class ClientPut(BaseModel):
    IdClasse: int
    IdNatureIdt: int
    IdPays: int
    NatureClient: str
    Etat: str
    IdCategorieAvoir: int
    RaisonSociale: str
    Matricule: str

    class Config():
        orm_mode = True


class CompteOutput(BaseModel):
    IdCompte: int
    IdClient: int
    IdDepositaire: int
    DateCreation: date
    Web: str
    Etat: str

    class Config():
        orm_mode = True


class TransactionOutput(BaseModel):
    IdImputation: int
    IdCompteEspece: int
    Montant: float
    Sens: int
    DateImputation: date
    IdDateImputation: int
    IdSDBCompte: int
    DateValeur: date
    IdDateValeur: int
    Nature: str
    Etat: int
    DateEtat: date
    libelle: str

    class Config():
        orm_mode = True







class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None