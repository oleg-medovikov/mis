# Полключение к базе данных
from .postgress import metadata, POSTGRESS_DB, POSTGRESS_EN

# Таблицы:
from .Person import t_Person
"""
Комплексный тип Person предназначен для передачи данных о лице
- участнике случая обслуживания. По-русски это пациент.
"""
from .HumanName import t_HumanName
"""
Комплексный тип HumanName предназначен для передачи ФИО персоны.
"""
from .IdentityDocument import t_IdentityDocument
"""
Комплексный тип IdentityDocument предназначен 
для передачи сведений о конкретном документе персоны. 
"""
from .PersonWithIdentity import t_PersonWithIdentity
"""
Таблица для сопоставления пациентов и списка его документов
"""
from .MedicalStaff import t_MedicalStaff
"""
Комплексный тип MedicalStaff предназначен для передачи данных
о медицинском работнике.
"""



# Создание таблиц
metadata.create_all(POSTGRESS_EN)
