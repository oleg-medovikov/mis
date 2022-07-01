from .postgress import metadata

from sqlalchemy import Table, Column, String

t_PersonWithIdentity = Table(
    "PersonWithIdentity",
    metadata,
    Column('IdPersonMis', String), # Это UUID Person
    Column('Documents',   String), # Это UUID IdentityDocument
    )
