from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement

from .base_element import BaseElement

class PriceRangeSlider(BaseElement):
  price_rng_slider_locators = {
    "slider": (By.TAG_NAME, "ngx-slider"),
    "min_price": (By.CSS_SELECTOR, ".ngx-slider-model-value"),
    "max_price": (By.CSS_SELECTOR, ".ngx-slider-model-high"),
    "min_pointer": (By.CSS_SELECTOR, ".ngx-slider-pointer-min"),
    "max_pointer": (By.CSS_SELECTOR, ".ngx-slider-pointer-max"),
  }

  def __init__(self, driver: WebDriver, filters_container: WebElement) -> None:
    super().__init__(driver)
    self.container = filters_container

  @property
  def slider(self):
    return self.container.find_element(*self.price_rng_slider_locators.get("slider"))
  
  @property
  def current_min_price(self):
    return self.container.find_element(*self.price_rng_slider_locators.get("min_price"))
  
  @property
  def current_max_price(self):
    return self.container.find_element(*self.price_rng_slider_locators.get("max_price"))
  
  @property
  def pointer_min(self):
    return self.container.find_element(*self.price_rng_slider_locators.get("min_pointer"))
  
  @property
  def pointer_max(self):
    return self.container.find_element(*self.price_rng_slider_locators.get("max_pointer"))