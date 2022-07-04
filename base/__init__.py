# Полключение к базе данных
from .postgress import metadata, POSTGRESS_DB, POSTGRESS_EN

# Таблицы:
from .Person import t_Person
"""
Комплексный тип Person предназначен для передачи данных о лице
- участнике случая обслуживания. По-русски это пациент.
Но туда же пишутся данные о врача, ибо почему нет.
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
from .BirthPlace import t_BirthPlace
"""
Место, где хранится место рождения пациента
"""
from .ContactDto import t_ContactDto
"""
Контактные данные персоны
"""
from .AddressDto import t_AddressDto
"""
Таблица для хранения адресов Person
"""
from .Guardian import t_Guardian
"""
Комплексный тип Guardian служит для передачи сведений 
о законном представителе пациента.
"""

# Создание 
metadata.create_all(POSTGRESS_EN)
