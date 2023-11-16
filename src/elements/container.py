from random import choice
from selenium.webdriver.common.by import By

from .base_element import BaseElement


class Container(BaseElement):
  locators = {
    "container": (By.CSS_SELECTOR, "div[data-test='']"),
    "card": (By.CSS_SELECTOR, "a.card")
  }

  @property
  def container(self):
    return self.driver.find_element(self.locators.get("container"))

  @property
  def cards(self):
    return self.driver.find_elements(*self.locators.get("card"))

  @property
  def random_card(self):
    return choice(self.cards)

  def is_container_present(self):
    return super().is_present(self.locators.get("container"))
  
  def is_cards_present(self):
    return super().is_all_present(self.locators.get("card"))
  
  def is_cards_visible(self):
    return super().is_all_visible(self.locators.get("card"))
  
  def is_cards_clickable(self):
    return super().is_all_clickable(self.locators.get("card"))
