from selenium.webdriver.common.by import By

from .base_element import BaseElement
from src.elements.sort import Sort
from src.elements.search import Search
from src.elements.price_range import PriceRangeSlider

class Filters(BaseElement):
  filter_locators = {
    "filter_container": (By.CSS_SELECTOR, "div[data-test='filters']")
  }

  @property
  def filters_container(self):
    return self.driver.find_element(*self.filter_locators.get("filter_container"))
  
  @property
  def sort(self):
    return Sort(self.driver, self.filters_container)
  
  @property
  def search(self):
    return Search(self.driver, self.filters_container)
  
  @property
  def price_range_slider(self):
    return PriceRangeSlider(self.driver, self.filters_container)
