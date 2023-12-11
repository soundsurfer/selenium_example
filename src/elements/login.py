from selenium.webdriver.common.by import By

from .base_element import BaseElement

class LoginForm(BaseElement):
  login_form_locators = {
    "title": (By.TAG_NAME, "h3"),
    "email": (By.ID, "email"),
    "password": (By.ID, "password"),
    "login_btn": (By.CSS_SELECTOR, "input[data-test='login-submit']"),
    "sign_in_google": (By.CLASS_NAME, "google-sign-in-button"),
    "register_link": (By.CSS_SELECTOR, "a[data-test='register-link']"),
    "forgot_pwd_link": (By.CSS_SELECTOR, "a[data-test='forgot-password-link']"),
    "email_error": (By.CSS_SELECTOR, "div[data-test='email-error']"),
    "pwd_error": (By.CSS_SELECTOR, "div[data-test='password-error']"),
    "login_error": (By.CSS_SELECTOR, "div[data-test='login-error']"),
  }

  @property
  def title(self):
    return self.driver.find_element(*self.login_form_locators.get("title"))

  @property
  def email(self):
    return self.driver.find_element(*self.login_form_locators.get("email"))

  @property
  def password(self):
    return self.driver.find_element(*self.login_form_locators.get("password"))

  @property
  def login_btn(self):
    return self.driver.find_element(*self.login_form_locators.get("login_btn"))

  @property
  def sign_in_with_google_btn(self):
    return self.driver.find_element(*self.login_form_locators.get("sign_in_google"))

  @property
  def register_link(self):
    return self.driver.find_element(*self.login_form_locators.get("register_link"))

  @property
  def forgot_pwd_link(self):
    return self.driver.find_element(*self.login_form_locators.get("forgot_pwd_link"))
  
  @property
  def email_error(self):
    return self.driver.find_element(*self.login_form_locators.get("email_error"))
  
  @property
  def pwd_error(self):
    return self.driver.find_element(*self.login_form_locators.get("pwd_error"))
  
  @property
  def login_error(self):
    return self.driver.find_element(*self.login_form_locators.get("login_error"))
  
  @property
  def email_error_text(self):
    return self.email_error.find_element(By.TAG_NAME, "div")

  @property
  def pwd_error_text(self):
    return self.pwd_error.find_element(By.TAG_NAME, "div")

  @property
  def login_error_text(self):
    return self.login_error.find_element(By.TAG_NAME, "div")
  
  def is_email_error_text_eq(self, exp_text: str):
    by, locator = self.login_form_locators.get("email_error")
    locator = locator + " > div" 
    return super().is_elem_text_eq((by, locator), exp_text)
  
  def is_pwd_error_text_eq(self, exp_text: str):
    by, locator = self.login_form_locators.get("pwd_error")
    locator = locator + " > div" 
    return super().is_elem_text_eq((by, locator), exp_text)

  def is_login_error_text_eq(self, exp_text: str):
    by, locator = self.login_form_locators.get("login_error")
    locator = locator + " > div" 
    return super().is_elem_text_eq((by, locator), exp_text)
  
  def fill_login_form(self, email: str, password: str):
    self.email.send_keys(email)
    self.password.send_keys(password)
  
