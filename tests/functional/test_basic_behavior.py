"""Basic behavior feature tests."""
import pytest
from pytest_bdd import given, scenario, then, when
from splinter import Browser
from splinter.config import Config
import os
from urllib.parse import urljoin


@pytest.fixture(scope='session')
def splinter_config():
    """Return a Splinter Config object."""
    headless = os.environ.get('HEADLESS', 'true').lower() == 'true'
    return Config(headless=headless)


@pytest.fixture(scope='session')
def splinter_browser(splinter_config):
    """Provide a browser instance using Splinter Config."""
    with Browser('chrome', config=splinter_config) as browser:
        yield browser


@pytest.fixture
def step_context():
    """Fixture to save information to use through steps."""
    return {}


@scenario('basic_behavior.feature', 'Home Page')
def test_home_page():
    """Home Page."""


@given('Calibre web is running')
def _(step_context):
    """Calibre web is running."""
    step_context['ip_address'] = 'localhost:8083'


@when('I go to the home page')
def _(splinter_browser, step_context):
    """I go to the home page."""
    url = urljoin(f"http://{step_context['ip_address']}", '/')
    splinter_browser.visit(url)


@then('I should not see the error message')
def _(splinter_browser):
    """I should not see the error message."""


@then('see homepage information')
def _(splinter_browser):
    """see homepage information."""
    print("!!!!!!!")
    print(splinter_browser.title)
    print(splinter_browser.url)
    print("!!!!!!!")
    assert splinter_browser.is_text_present('Books'), 'Book test'


@scenario('basic_behavior.feature', 'Login')
def test_login():
    """Login."""


@given('I visit the calibre web homepage')
def _(splinter_browser, step_context):
    """I visit the calibre web homepage."""
    step_context['ip_address'] = 'localhost:8083'
    url = urljoin(f"http://{step_context['ip_address']}", '/')
    splinter_browser.visit(url)


@when('I login with valid credentials')
def _(splinter_browser):
    """I login with valid credentials."""
    splinter_browser.fill('username', 'Admin')
    splinter_browser.fill('password', 'changeme')
    button = splinter_browser.find_by_name('submit')
    # Interact with elements
    button.click()


@then('I should see the success message')
def _(splinter_browser):
    """I should see the success message."""
    assert splinter_browser.is_text_present('You are now logged in as:'), 'Login successful'


@then('see the information for logged users')
def _(splinter_browser):
    """see the information for logged users"""
    assert splinter_browser.is_text_present('Books'), 'Expected "Books" text to be visible on the home page'
    assert splinter_browser.is_text_present('Download to IIAB'), 'Expected "Download to IIAB" button for logged users'
