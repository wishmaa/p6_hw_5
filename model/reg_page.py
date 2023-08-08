import os

from selene import browser, have
from selene import command


class RegPage:
    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)
        return self

    def fill_firstname(self, value):
        browser.element("#firstName").type(value)

    def fill_lastname(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def fill_gender(self, value):
        browser.all("#genterWrapper .custom-control").element_by(
            have.exact_text(value)
        ).click()

    def fill_phone(self, value):
        browser.element("#userNumber").type(value)

    def fill_dateofbirth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)"
        ).click()

    def fill_subjects(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def fill_hobby(self, value):
        browser.all(".custom-checkbox").element_by(have.exact_text(value)).click()

    def upload_file(self, value):
        return str(
            browser.element("#uploadPicture").send_keys(
                os.path.abspath(f"picture/{value}")
            )
        )

    def fill_currentadress(self, value):
        browser.element("#currentAddress").type(value)

    def fill_state(self, value):
        browser.element("#state").click()
        browser.all("#state div").element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element("#city").click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        browser.element('#submit').perform(command.js.click)

    def should_have_header(self, value):
        browser.element("#example-modal-sizes-title-lg").should(have.text(value))

    def should_have_user_information(
            self, full_name, email, gender, phone, date_birth, subject, hobby, file, address, city_state):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_birth,
                subject,
                hobby,
                file,
                address,
                city_state
            )
        )
        return self
