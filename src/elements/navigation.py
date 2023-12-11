from selenium.webdriver.common.by import By

from .base_element import BaseElement

class Navigation(BaseElement):
  navigation_categories = {
    "home": (By.CSS_SELECTOR, "a[data-test='nav-home']"),
    "categories": (By.CSS_SELECTOR, "a[data-test='nav-categories']"),
    "contact": (By.CSS_SELECTOR, "a[data-test='nav-contact']"),
    "login": (By.CSS_SELECTOR, "a[data-test='nav-sign-in']"),
  }

  user_navigation_categories ={
    "user_menu": (By.CSS_SELECTOR, "a[data-test='nav-user-menu']")
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
  def user_menu(self):
    return self.driver.find_element(*self.user_navigation_categories.get("user_menu"))

  @property
  def user_menu_options(self):
    return self.driver.find_elements(By.CSS_SELECTOR, "a")

  @property
  def category_items(self):
    return self.categories.find_elements(By.CSS_SELECTOR, "a")

  def is_nav_category_present(self, category_name: str):
    if not isinstance(category_name, str):
      raise ValueError("Category name should be a string!")

    categories = self.navigation_categories | self.user_navigation_categories

    if category_name in categories:
      return super().is_present(categories.get(category_name))
    else:
      raise KeyError("Unknown category!")
  
  def is_nav_category_clickable(self, category_name: str):
    if not isinstance(category_name, str):
      raise ValueError("Category name should be a string!")
    
    categories = self.navigation_categories | self.user_navigation_categories

    if category_name in categories:
      return super().is_clickable(categories.get(category_name))
    else:
      raise KeyError("Unknown category!")
  
  def is_nav_category_visible(self, category_name: str):
    if not isinstance(category_name, str):
      raise ValueError("Category name should be a string!")
    
    categories = self.navigation_categories | self.user_navigation_categories

    if category_name in categories:
      # TODO: Do not rely on this. 
      # If we have some prop that wasn't listed in locators it won't see it.
      return super().is_visible(getattr(self, category_name))
    else:
      raise KeyError("Unknown category!")
    
  def is_all_nav_categories_present(self, login=False):
    # TODO: Remove repetition.
    _nav_categories = self.navigation_categories

    if login:
      _nav_categories = self.navigation_categories[:-1]
      _nav_categories.update(self.user_navigation_categories.items())
      
    return all(self.is_nav_category_present(category_name=category) for category in _nav_categories)
  
  def is_all_nav_categories_visible(self, login=False):
    _nav_categories = self.navigation_categories
    
    if login:
      _nav_categories = self.navigation_categories[:-1]
      _nav_categories.update(self.user_navigation_categories.items())
    
    return all(self.is_nav_category_visible(category_name=category) for category in _nav_categories)
  
  def is_all_nav_categories_clickable(self, login=False):
    _nav_categories = self.navigation_categories
    
    if login:
      _nav_categories = self.navigation_categories[:-1]
      _nav_categories.update(self.user_navigation_categories.items())

    return all(self.is_nav_category_clickable(category_name=category) for category in _nav_categories)