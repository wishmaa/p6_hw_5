import datetime
from model.pages.reg_page import RegPage
from model.users.users import User


def test_fill_form():
    # Open registration form
    reg_page = RegPage()

    Newreguser = User(
        first_name='petr',
        last_name='Lastname',
        email='testnew@mail.ru',
        gender='Male',
        phone='1234567890',
        birthday=datetime.date(1991, 2, 10),
        subjects='Computer Science',
        hobby='Music',
        image='image.png',
        address='Ulitsa',
        state='NCR',
        city='Delhi'
    )

    reg_page.open()
    reg_page.fill_all_form(Newreguser)
    reg_page.should_have_user_information(Newreguser)
