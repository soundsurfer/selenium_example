from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement

from .base_element import BaseElement

class Search(BaseElement):
  search_locators = {
    "search_field": (By.CSS_SELECTOR, "input[data-test='search-query']"),
    "search_reset": (By.CSS_SELECTOR, "button[data-test='search-reset']"),
    "search_submit": (By.CSS_SELECTOR, "button[data-test='search-submit']"),
  }

  def __init__(self, driver: WebDriver, filters_container: WebElement) -> None:
    super().__init__(driver)
    self.container = filters_container

  @property
  def search_field(self):
    return self.container.find_element(*self.search_locators.get("search_field"))
  
  @property
  def search_reset_btn(self):
    return self.container.find_element(*self.search_locators.get("search_reset"))
  
  @property
  def search_submit_btn(self):
    return self.container.find_element(*self.search_locators.get("search_submit"))
  
  def is_search_reset_btn_clickable(self):
    return super().is_clickable(self.search_locators.get("search_reset"))

  def is_search_submit_btn_clickable(self):
    return super().is_clickable(self.search_locators.get("search_submit"))