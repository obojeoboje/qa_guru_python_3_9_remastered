from datetime import date
import allure
from demoqa_tests.modules.data.user import User
from demoqa_tests.modules.pages.practice_form import PracticeForm


def test_registration_user():
    practice_form = PracticeForm()
    user = User(
        first_name='Aleksandr',
        last_name='Privalov',
        email='obojealexander@gmail.com',
        phone='1234567890',
        address='Saint Petersburg',
        birthday=date(1999, 5, 27),
        gender='Male',
        subject='Computer Science',
        hobbies='Music',
        image='picture.jpg',
        state='NCR',
        city='Delhi')

    with allure.step('Открыть форму регистрации'):
        practice_form.open_page()
    with allure.step('Заполнить форму'):
        practice_form.fill(user).submit()
    with allure.step('Проверить результаты с введенными нами выше'):
        practice_form.assert_results_registration(user)
        practice_form.proceed_attachments()
