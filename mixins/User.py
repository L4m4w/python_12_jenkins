from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from mixins import registration_form_page

class Gender(Enum):
    male = "Male"
    female = "Female"
    other = "Other"

class Hobbies(Enum):
    sport = "Sports"
    reading = "Reading"
    music = "Music"

class State(Enum):
    ncr = "NCR"
    uttar_pradesh = "Uttar Pradesh"
    haryana = "Haryana"
    rajasthan = "Rajasthan"


@dataclass
class User:
    first_name: str = ''
    last_name: str = ''
    email: str = ''
    gender: Gender = ''
    mobile_number: str = ''
    birth_date: datetime.date = registration_form_page.RegistrationFormPage.current_date()
    subject: str = ''
    hobbies: Hobbies = ''
    picture: str = ''
    address: str = ''
    state: State = ''
    city: str = ''