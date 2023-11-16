from .base_page import BasePage
from src.elements.header import Header
from src.elements.container import Container
from src.elements.pagination import Pagination

class HomePage(BasePage):

  def open(self):
    return super().open("#")
  
  @property
  def header(self):
    return Header(self.driver)

  @property
  def card_container(self):
    return Container(self.driver)
  
  @property
  def pagination(self):
    return Pagination(self.driver)
  