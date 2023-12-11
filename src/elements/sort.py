from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement

from .base_element import BaseElement

class Sort(BaseElement):
  sort_locators = {
    "sort": (By.CSS_SELECTOR, "select[data-test='sort']"),
    "options": (By.TAG_NAME, "option"),
  }

  def __init__(self, driver: WebDriver, filters_container: WebElement) -> None:
    super().__init__(driver)
    self.container = filters_container

  @property
  def sort(self):
    return self.container.find_element(*self.sort_locators.get("sort"))
  
  @property
  def sort_options(self):
    return self.sort.find_elements(*self.sort_locators.get("options"))