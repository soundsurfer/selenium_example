from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .navigation import Navigation

class Header(BaseElement):
  locators = {
    "brand_img": (By.CSS_SELECTOR, "a.navbar-brand")
  }

  @property
  def brand_img(self):
    return self.driver.find_element(*self.locators.get("brand_img"))

  def is_brand_img_present(self):
    return super().is_present(self.locators.get("brand_img"))

  @property
  def navigation(self):
    return Navigation(self.driver)
