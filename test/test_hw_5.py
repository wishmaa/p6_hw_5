
from model.reg_page import RegPage


def test_fill_form():
    # Open registration form
    reg_page = RegPage()
    reg_page.open()

    # Fill form
    reg_page.fill_firstname('Name')

    reg_page.fill_lastname('Lastname')

    reg_page.fill_email('mailemail@mail.com')

    reg_page.fill_gender('Male')

    reg_page.fill_phone('8922132234')

    reg_page.fill_dateofbirth('1990', 'February', '09')

    reg_page.fill_subjects('Computer Science')

    reg_page.fill_hobby('Reading')

    reg_page.upload_file('image.png')

    reg_page.fill_currentadress('127000 Main Street 12b')

    reg_page.fill_state('NCR')

    reg_page.fill_city('Delhi')

    # Check registration results
    reg_page.should_have_header('Thanks for submitting the form')

    reg_page.should_have_user_information(
        'Name Lastname',
        'mailemail@mail.com',
        'Male',
        '8922132234',
        '09 February,1990',
        'Computer Science',
        'Reading',
        'image.png',
        '127000 Main Street 12b',
        'NCR Delhi',
    )
