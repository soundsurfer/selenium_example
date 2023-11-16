from selenium.webdriver.common.by import By

from .base_element import BaseElement

class Navigation(BaseElement):
  navigation_categories = {
    "home": (By.CSS_SELECTOR, "a[data-test='nav-home']"),
    "categories": (By.CSS_SELECTOR, "a[data-test='nav-categories']"),
    "contact": (By.CSS_SELECTOR, "a[data-test='nav-contact']"),
    "login": (By.CSS_SELECTOR, "a[data-test='nav-sign-in']"),
  }

  navigation_locators = {
    "category_items": (By.CSS_SELECTOR, "a")
  }

  @property
  def home(self):
    return self.driver.find_element(*self.navigation_categories.get("home"))

  @property
  def categories(self):
    return self.driver.find_element(*self.navigation_categories.get("categories"))

  @property
  def contact(self):
    return self.driver.find_element(*self.navigation_categories.get("contact"))
  
  @property
  def login(self):
    return self.driver.find_element(*self.navigation_categories.get("login"))

  @property
  def category_items(self):
    return self.categories.find_elements(*self.navigation_locators.get("category_items"))

  def is_nav_category_present(self, category_name: str):
    if not isinstance(category_name, str):
      raise ValueError("Category name should be a string!")

    if category_name in self.navigation_categories:
      return super().is_present(self.navigation_categories.get(category_name))
    else:
      raise KeyError("Unknown category!")
  
  def is_nav_category_clickable(self, category_name: str):
    if not isinstance(category_name, str):
      raise ValueError("Category name should be a string!")

    if category_name in self.navigation_categories:
      return super().is_clickable(self.navigation_categories.get(category_name))
    else:
      raise KeyError("Unknown category!")
  
  def is_nav_category_visible(self, category_name: str):
    if not isinstance(category_name, str):
      raise ValueError("Category name should be a string!")

    if category_name in self.navigation_categories:
      # TODO: Do not rely on this. 
      # If we have some prop that wasn't listed in locators it won't see it.
      return super().is_visible(getattr(self, category_name))
    else:
      raise KeyError("Unknown category!")
    
  def is_all_nav_categories_present(self):
    return all(self.is_nav_category_present(category_name=category) for category in self.navigation_categories)
  
  def is_all_nav_categories_visible(self):
    return all(self.is_nav_category_visible(category_name=category) for category in self.navigation_categories)
  
  def is_all_nav_categories_clickable(self):
    return all(self.is_nav_category_clickable(category_name=category) for category in self.navigation_categories)