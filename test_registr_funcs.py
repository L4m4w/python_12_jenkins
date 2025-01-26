import os
import time

from selene import have, be, browser
# from selene.support.shared import browser

from mixins.application import app
from mixins.User import User, Gender
from mixins.registratio_form_page import RegistrationFormPage

"""
Разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form

1. Find the field;
2. Fill the field;
3. Fill the form;
4. Submit the form;
5. Eat cookie (no sugar, low fat)

Requirements:
Name - First name/ Last name - input text id: firstName; input id: lastName
Gender (battle helicopter) - input radiobuttons id:gender-radio-1; gender-radio-2; gender-radio-3
Mobile (10 digits) - input text id="userNumber" minlength="10"/ maxlength="10"

Optional:
Email - text id: userEmail pattern="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
Date of Birth - id="dateOfBirthInput" value="03 Apr 2022"
Subjects - id="subjectsInput"
choose Hobbies - input checkbox id:hobbies-checkbox-1; hobbies-checkbox-2; hobbies-checkbox-3
select and upload a Picture - id: uploadPicture
Current Address - id="currentAddress"
State and city - dropdowns - id="react-select-3-input"; id="react-select-4-input"

Submit - id="submit"
"""

PICTURE_NAME = "img-1.png"

def test_form_fill_app_method():
    # Application Management
    pashu = User(first_name='Abc1', last_name='Abc1', gender=Gender.male.value, mobile_number='1234567890')
    # print(pashu)
    app.simple_registration.open()
    app.register(pashu)
    app.should_have_registrated(pashu)

def test_full_form_fill():
    registration_page = RegistrationFormPage()

    # Simple page object
    registration_page.open()

    registration_page.fill_first_name('Abc1')

    registration_page.fill_last_name('Abc1')

    registration_page.fill_email('name@example.com')

    registration_page.choose_gender('Female')

    registration_page.fill_phone_number('1234567890')

    registration_page.fill_date_of_birth('2024', 'April', '11')

    # browser.element("//div[@aria-label='Choose Tuesday, April 16th, 2024']").perform(command.js.click)

    registration_page.fill_subject('English')

    registration_page.choose_hoobie('Reading')

    registration_page.upload_picture(PICTURE_NAME)

    registration_page.fill_current_address('Lenins street')

    registration_page.select_state('NCR')

    registration_page.select_city('Delhi')

    registration_page.submit_registration_page()

    registration_page.should_registrated_form('Abc1', 'Abc1',
                'name@example.com',
                'Female',
                '1234567890',
                '11 April,2024',
                'English',
                'Reading',
                'img-1.png',
                'Lenins street',
                'NCR',
                'Delhi')


def test_requirements_form_fill():
    registration_page = RegistrationFormPage()

    registration_page.open()

    registration_page.fill_first_name('abc')
    registration_page.fill_last_name('efg')
    registration_page.choose_gender('Male')
    registration_page.fill_phone_number('1234567890')

    registration_page.submit_registration_page()

    registration_page.should_registrated_form(first_name='abc', last_name='efg',gender='Male',
                                              mobile_number='1234567890')