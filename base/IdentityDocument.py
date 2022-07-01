from .postgress import metadata

from sqlalchemy import Table, Column, SmallInteger, String, DateTime

t_IdentityDocument = Table(
    "IdentityDocument",
    metadata,
    Column('DocN',           String), # Номер документа
    Column('DocS',           String), # Серия документа
    Column('DocumentName',   String), # Наименование документа (не используется для передачи в сервис)
    Column('ExpiredDate',    DateTime), # Дата окончания действия документа
    Column('IdDocumentType', SmallInteger), # Типа документа (Справочник OID: 1.2.643.2.69.1.1.1.6)
    #=== Если документ - это полис:
    Column('IdPovider',    String), # Код организации, выдавшей документ. (Справочник OID:1.2.643.5.1.13.2.1.1.635)
    #==========
    Column('IssuedDate',   DateTime), # Дата выдачи документа
    Column('ProviderName', String), # Наименование организации, выдавшей документ 
    Column('RegionCode',   String), # Код территории страхования (для полиса)
    Column('StartDate',    DateTime), # Дата начала действия документа
    )
