from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from src.elements.header import Header

class AccountPage(BasePage):

  account_page_locators = {
    "title": (By.CSS_SELECTOR, "h1[data-test='page-title']")
  }

  def open(self):
    return super().open("#/account")
  
  @property
  def header(self):
    return Header(self.driver)

  @property
  def title(self):
    return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_page_locators.get("title")))

  @property
  def favorites(self):
    pass

  @property
  def profile(self):
    pass

  @property
  def invoices(self):
    pass

  @property
  def messages(self):
    pass
  