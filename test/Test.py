from selene import browser, have, be
import os

def test_fill_form():
    browser.open('/automation-practice-form')
    browser.should(have.url_containing('automation-practice-form'))

#Fill form
    browser.element('#firstName').type('Name')
    browser.element('#lastName').type('Lastname')
    browser.element('#userEmail').type('mailemail@mail.com')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('8922132234')

#Date birth
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="1990"]').click()
    browser.element('[value="2"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--009"]').click()

#Hobby
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()

#Upload file
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/image.png'))

#City
    browser.element('#currentAddress').type("127000 Main Street 12b")
    browser.element('#state').click()
    browser.all('#state div').element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all('#city div').element_by(have.exact_text("Delhi")).click()
    browser.element('#submit').click()

#Check form
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Name Lastname'))
    browser.element('.modal-body').should(have.text('mailemail@mail.com'))
    browser.element('.modal-body').should(have.text('Male'))
    browser.element('.modal-body').should(have.text('8922132234'))
    browser.element('.modal-body').should(have.text('09 March,1990'))
    browser.element('.modal-body').should(have.text('Computer Science'))
    browser.element('.modal-body').should(have.text('Sports'))
    browser.element('.modal-body').should(have.text('image.png'))
    browser.element('.modal-body').should(have.text('127000 Main Street 12b'))
    browser.element('.modal-body').should(have.text('NCR Delhi'))