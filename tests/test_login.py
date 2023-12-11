import pytest

from config import TEST_EMAIL, TEST_PASS

from src.pages.login import LoginPage
from src.pages.account import AccountPage

@pytest.fixture()
def login_page(browser):
  login_page = LoginPage(browser)

  login_page.open()

  yield login_page

  login_page.driver.delete_all_cookies()
  login_page.driver.refresh()

def test_login_form_elements(login_page):
  assert login_page.login_form.title.is_displayed()
  assert login_page.login_form.email.is_displayed()
  assert login_page.login_form.password.is_displayed()
  assert login_page.login_form.login_btn.is_displayed()
  assert login_page.login_form.login_btn.is_displayed()
  assert login_page.login_form.sign_in_with_google_btn.is_displayed()
  assert login_page.login_form.register_link.is_displayed()
  assert login_page.login_form.forgot_pwd_link.is_displayed()

def test_sing_in_with_existing_user_acc(login_page, browser):
  account_page = AccountPage(browser)
  
  login_page.login_form.fill_login_form(TEST_EMAIL, TEST_PASS)
  login_page.login_form.login_btn.click()
  assert account_page.header.navigation.is_nav_category_present("user_menu")

def test_sign_in_with_non_existing_user_acc(login_page):
  login_page.login_form.fill_login_form("johndoe@email.com", "qwerty")
  login_page.login_form.login_btn.click()

  assert login_page.login_form.is_login_error_text_eq("Invalid email or password")

def test_sign_in_with_invalid_pass(login_page):
  login_page.login_form.fill_login_form(TEST_EMAIL, "qwerty")
  login_page.login_form.login_btn.click()

  assert login_page.login_form.is_login_error_text_eq("Invalid email or password")

def test_sign_in_required_pass_alert(login_page):
  login_page.login_form.fill_login_form("johndoe@email.com", "")
  login_page.login_form.login_btn.click()
  login_page.login_form.password.clear()

  assert login_page.login_form.is_pwd_error_text_eq("Password is required.")

def test_sign_in_required_email_alert(login_page):
  login_page.login_form.fill_login_form("", "qwerty")
  login_page.login_form.login_btn.click()
  login_page.login_form.email.clear()

  assert login_page.login_form.is_email_error_text_eq("E-mail is required.")

def test_sign_in_invalid_email_alert(login_page):
  login_page.login_form.fill_login_form("qwerty@qwerty", "qwerty")
  login_page.login_form.login_btn.click()

  assert login_page.login_form.is_email_error_text_eq("E-mail format is invalid.")
