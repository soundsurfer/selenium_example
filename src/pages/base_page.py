from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
  def __init__(self, driver: WebDriver) -> None:
    self.driver = driver

  def open(self, path):
    self.driver.get(f"https://practicesoftwaretesting.com/{path}")

  def close(self):
    self.driver.close()