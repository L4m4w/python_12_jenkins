# from selene import browser
from selene.support.shared import browser

from .registratio_form_page import RegistrationFormPage
from .User import User


class Application(User):
    def __init__(self):
        self.simple_registration = RegistrationFormPage()
        # self.user = User()

    def open(self):
        browser.open_url('/')
        return self

    def register(self, user):
        # return user.first_name
        self.simple_registration.fill_first_name(user.first_name)
        self.simple_registration.fill_last_name(user.last_name)
        self.simple_registration.choose_gender(user.gender)
        self.simple_registration.fill_phone_number(user.mobile_number)
        self.simple_registration.submit_registration_page()

    def should_have_registrated(self, user):
        self.simple_registration.should_registrated_form(
            first_name=user.first_name, last_name=user.last_name, mail=user.email, gender=user.gender,
            mobile_number=user.mobile_number, birthdate=user.birth_date, subject=user.subject,
            hobbie=user.hobbies, picture=user.picture, current_address=user.address, state=user.state, city=user.city)



app = Application()