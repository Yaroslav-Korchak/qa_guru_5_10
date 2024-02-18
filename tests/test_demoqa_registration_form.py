from selene import browser, have, by, command
import os



def test_fill_in_registration_form_successful():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Yar')
    browser.element('#lastName').type('Korchak')
    browser.element('#userEmail').type('name@example.com')
    browser.element('[value=Male]+label').click()
    browser.element('#userNumber').type('9001234567')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1989"]').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('January')).click()
    browser.element(f'.react-datepicker__day--0{'01'}').click()

    browser.element('#subjectsInput').type('c')
    browser.element('//div[contains(text(), "Civics")]').perform(command.js.scroll_into_view).click()
    browser.element('//label[contains(text(), "Music")]').click()

    browser.element('#uploadPicture').send_keys(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'data/YLhdScg4g_4.jpg')))

    browser.element('#currentAddress').perform(command.js.scroll_into_view).send_keys('Paramaribo, Green Street 568')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Rajasthan')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Jaiselmer')).click()

    browser.element('#submit').click()

    browser.element('.table').all('td').even.should(have.texts('Yar Korchak', 'name@example.com', 'Male',
                                                               '9001234567',
                                                               '01 January,1989', 'Civics', 'Music', 'YLhdScg4g_4.jpg',
                                                               'Paramaribo, Green Street 568', 'Rajasthan Jaiselmer'))

    browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()




