from selene import browser
import pytest

@pytest.fixture
def browser_config():
	browser.config.base_url = "https://todomvc.com/examples"

def test_complete_todo():
	browser.open("/emberjs/todomvc/dist/")