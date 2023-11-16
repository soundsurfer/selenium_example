import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
  driver = webdriver.Chrome()
  driver.maximize_window()
  yield driver
  driver.quit()