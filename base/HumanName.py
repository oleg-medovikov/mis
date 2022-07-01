from .postgress import metadata

from sqlalchemy import Table, Column, Integer, String

t_HumanName = Table(
    "HumanName",
    metadata,
    Column('UUID',       String), # Идентификатор строки
    Column('GivenName',  String), # Имя
    Column('MiddleName', String), # Отчество
    Column('FamilyName', String), # Фамилия
    )
