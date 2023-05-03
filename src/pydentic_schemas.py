from pydantic import BaseModel, validator, HttpUrl, EmailStr  # UUID4
from src.enums import Status, Gender, UserErrors
from pydantic.types import PastDate, FutureDate  # PaymentCardNumber
# from pydantic.types import List
from pydantic.color import Color


class Post(BaseModel):  # Set the structure of the object.
    id: int  # = Field(le=2) ## Check that the id is not greater than 2
    title: str

    @validator("id")  # Create our own validator.
    def validate_id_less_than(cls, max_id):
        if max_id > 3:
            raise ValueError("Id is not less than two")
        else:
            return max_id


class GorestGetUsers(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status

    @validator('email')
    def is_dog_in_email(cls, email):
        if "@" in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)


class Technical(BaseModel):
    body: str
    color: Color
    weight: int
    photo: HttpUrl


class Owners(BaseModel):
    name: str
    card_number: str  # PaymentCardNumber
    email: EmailStr


class DetailedInformation(BaseModel):
    technical: Technical
    owners: Owners


class Cars(BaseModel):
    id: str
    mark: str
    model: str
    made_at: PastDate
    paid_for_parking_until: FutureDate
    VIN: str
    status: str
    detailed_information: DetailedInformation
