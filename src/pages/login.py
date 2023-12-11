from .base_page import BasePage
from src.elements.login import LoginForm
from src.elements.header import Header

class LoginPage(BasePage):
  def open(self):
    return super().open("#/auth/login")
  
  def close(self):
    return super().close()

  @property
  def header(self):
    return Header(self.driver)
  
  @property
  def login_form(self):
    return LoginForm(self.driver)
