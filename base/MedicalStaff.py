from .postgress import metadata

from sqlalchemy import Table, Column, String, SmallInteger

t_MedicalStaff = Table(
    "MedicalStaff",
    metadata,
    Column('IdPersonMis', String), # Это UUID Person
    Column('IdLpu', String),
    # Код подразделения (Справочник МО oid 1.2.643.2.69.1.1.1.64) 
    Column('IdSpeciality', SmallInteger),   
    # Код специальности (Справочник OID 1.2.643.5.1.13.2.1.1.181)
    Column('IdPosition', SmallInteger),
    # Идентификатор должности (Справочник OID:1.2.643.5.1.13.2.1.1.607)
    Column('IdMedicalStaff', String), # Идентификатор записи в БД
    Column('PositionName', String),   # Наименование должности
    Column('SpecialityName', String), # Наименование специальности 
    )
