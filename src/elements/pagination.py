from selenium.webdriver.common.by import By

from .base_element import BaseElement

class Pagination(BaseElement):
  pagination_locators = {
    "pagination": (By.CSS_SELECTOR, "ul.pagination"),
    "previous": (By.CSS_SELECTOR, "a[aria-label='Previous']"),
    "next": (By.CSS_SELECTOR, "a[aria-label='Next']"),
    "pages": (By.CSS_SELECTOR, ".page-item > a")
  }

  @property
  def pagination(self):
    return self.driver.find_element(*self.pagination_locators.get("pagination"))

  @property
  def previous_btn(self):
    return self.driver.find_element(*self.pagination_locators.get("previous"))

  @property
  def next_btn(self):
    return self.driver.find_element(*self.pagination_locators.get("next"))

  @property
  def pages(self):
    return list(filter(lambda el: el.text.isnumeric() ,self.driver.find_elements(*self.pagination_locators.get("pages"))))
  
  def is_pagination_present(self):
    return super().is_present(self.pagination_locators.get("pagination"))
  
  def is_previous_btn_disabled(self):
    return not self.driver.find_element(*self.pagination_locators.get("previous")).is_enabled()
  
  def is_next_btn_clickable(self):
    return super().is_clickable(self.pagination_locators.get("next"))
