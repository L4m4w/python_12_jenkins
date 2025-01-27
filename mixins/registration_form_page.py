import os
from datetime import datetime
from time import daylight

from selene import have, command
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import allure

import tests as tests




def path(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )

class RegistrationFormPage:

    def __init__(self, browser_manager):
        self.browser = browser_manager


    def slide_to_submit_button(self):
        self.browser.scroll_to_element('#submit')

    @allure.step('Открываем главную страницу')
    def open(self):
        self.browser.open('https://demoqa.com/automation-practice-form/')

    @allure.step('Заполняем имя')
    def fill_first_name(self, value: str):
        """
        Fill first name in DOM element
        :param value:
        :return:
        """
        self.browser.element('#firstName').type(value)

    @allure.step('Заполняем фамилию')
    def fill_last_name(self, value: str):
        self.browser.element('#lastName').type(value)

    @allure.step('Заполняем поле email')
    def fill_email(self, value: str):
        self.browser.element('#userEmail').type(value)

    @allure.step('Заполняем поле пола')
    def choose_gender(self, value: str):
        self.browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    @allure.step('Заполняем поле номера телефона')
    def fill_phone_number(self, value: str):
        self.browser.element('#userNumber').type(value)

    @allure.step('Заполняем поле дата рождения')
    def fill_date_of_birth(self, year:str, month:str, day:str):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    @allure.step('Заполняем поле предмета')
    def fill_subject(self, value):
        self.browser.element('#subjectsInput').send_keys(value).press_enter()

    @allure.step('Заполняем поле хобби')
    def choose_hoobie(self, value):
        self.browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    @allure.step('Прикладываем картинку')
    def upload_picture(self, value):
        # self.browser.element('#uploadPicture').set_value(path(value))
        # goifa = 'C:\Users\larke\PycharmProjects\guru_in_py\python_10_9\resources\img-1.png'
        path = self.get_file_path_from_neighbor_folder('img-1.png')
        # absolute_path = os.path.abspath(path)
        self.browser.element('#uploadPicture').send_keys(path)

    def get_file_path_from_neighbor_folder(self, file_name: str):
        # Получаем путь к текущей директории
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Путь к соседней папке (например, предполагаем, что она находится на один уровень выше)
        neighbor_folder = os.path.join(current_dir, '..', 'resources')

        # Путь к файлу в соседней папке
        file_path = os.path.join(neighbor_folder, file_name)

        return os.path.abspath(file_path)

    @allure.step('Заполняем поле адреса')
    def fill_current_address(self, value):
        self.browser.element('#currentAddress').type(value)

    @allure.step('Заполняем поле Штата')
    def select_state(self, value):
        self.browser.element('#react-select-3-input').send_keys(value).press_tab()

    @allure.step('Заполняем поле города')
    def select_city(self, value):
        self.browser.element('#react-select-4-input').send_keys(value).press_tab()

    @allure.step('Завершаем заполениние формы')
    def submit_registration_page(self):
        # self.slide_to_submit_button()
        self.browser.element('#submit').send_keys(Keys.PAGE_DOWN)
        self.browser.element('#submit').click()

    @staticmethod
    def current_date():
        """
        :return: current date in right format
        """
        day = datetime.now().strftime('%d')
        month = datetime.now().strftime('%B')
        year = datetime.now().strftime('%Y')
        return f'{day} {month},{year}'

    @allure.step('Проверяем форму регистрации')
    def should_registrated_form(self, first_name='', last_name='', mail='', gender='',
                                mobile_number='', birthdate=current_date(), subject='', hobbie='',
                                picture='', current_address='', state='', city=''):
        """
        :param first_name:
        :param last_name:
        :param mail:
        :param gender:
        :param mobile_number:
        :param birthdate:
        :param subject:
        :param hobbie:
        :param picture:
        :param current_address:
        :param state:
        :param city:

        :return: Assert of form content
        """
        full_name = ' '.join(filter(None, [first_name, last_name]))
        state_city = ' '.join(filter(None, [state, city]))

        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                mail,
                gender,
                mobile_number,
                birthdate,
                subject,
                hobbie,
                picture,
                current_address,
                state_city
            )
        )
