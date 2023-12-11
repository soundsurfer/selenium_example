from typing import Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseElement:
  def __init__(self, driver: WebDriver) -> None:
    self.driver = driver

  def is_present(self, locator: tuple, wait: int = 10):
    return True if WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator)) else False

  def is_visible(self, element: WebElement, wait: int = 10):
    return True if WebDriverWait(self.driver, wait).until(EC.visibility_of(element=element)) else False

  def is_clickable(self, locator: Union[WebElement, tuple], wait: int = 10):
    return True if WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable(locator)) else False

  def is_all_present(self, locator: tuple, wait: int = 10):
    return True if WebDriverWait(self.driver, wait).until(EC.presence_of_all_elements_located(locator)) else False

  def is_all_visible(self, locator: tuple, wait: int = 10):
    return True if WebDriverWait(self.driver, wait).until(EC.visibility_of_all_elements_located(locator)) else False

  def is_all_clickable(self, locator: tuple, wait: int = 10):
    return all(self.is_clickable(elmt, wait=wait) for elmt in self.driver.find_elements(*locator))
  
  def is_elem_text_eq(self, locator: tuple, exp_text: str, wait: int = 10):
    return WebDriverWait(self.driver, wait).until(EC.text_to_be_present_in_element(locator, exp_text))

  def is_elem_has_attr(self, locator: tuple, attr: str, wait: int = 10):
    return WebDriverWait(self.driver, wait).until(EC.element_attribute_to_include(locator, attr))
  
  def is_elem_attr_has_text(self, locator: tuple, attr: str, exp_val: str, wait: int = 10):
    return WebDriverWait(self.driver, wait).until(EC.text_to_be_present_in_element_attribute(locator, attr, exp_val))
