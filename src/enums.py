from enum import Enum

class GlobalErrorMassages:
    WRONG_STATUS_CODE = 'Reseived status code is not equal to expected.'
    WRONG_NUMBER_ELEMENTS = 'Wrong number of elements in response'

class UserErrors(Enum):
    WRONG_EMAIL = "Email does not contain an '@' sign"

class Gender(Enum):
    male = "male"
    female = "female"

class Status(Enum):
    active = "active"
    inactive = "inactive"
