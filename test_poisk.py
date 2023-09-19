import pytest
from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene(open_browzer):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))


def test_google_should_not_find_result(open_browzer):
    browser.element('[name="q"]').should(be.blank).type('wetqwugdgdkshbcgdfkshdgfk').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
