import pytest

from main import base_sum

@pytest.fixture
def open_browser():
	print("\nStart browser for test")
	yield
	print("\nQuit browser after test")

@pytest.fixture
def browser_management(open_browser):
	print("Additional setup before test")
	yield
	print("Additional teardown after test")

@pytest.fixture
def user_data():
	print("Setup user data")
	yield {"username": "test_user", "password": "secure_pass"}
	print("Teardown user data")

def test_sum(browser_management, user_data):
	print(f"Testing with user: {user_data['username']}")
	assert base_sum(2, 3) == 5
	assert base_sum(-1, 1) == 0
	assert base_sum(0, 0) == 0
	assert base_sum(100, 200) == 300