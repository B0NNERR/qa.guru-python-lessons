from selene import browser
import pytest

@pytest.fixture(scope="session")
def browser_config():
	browser.config.base_url = 'https://google.com'
	browser.config.timeout = 5
	browser.config.window_width = 1920
	browser.config.window_height = 1080
	return browser