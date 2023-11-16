from src.pages.home import HomePage

def test_home_page_elements(browser):
  home_page = HomePage(browser)

  home_page.open()

  assert home_page.header.is_brand_img_present()
  assert home_page.header.navigation.is_all_nav_categories_visible()
  assert home_page.header.navigation.is_all_nav_categories_clickable()

  assert home_page.card_container.is_container_present()
  assert home_page.card_container.is_cards_visible()
  assert home_page.card_container.is_cards_clickable()
  assert len(home_page.card_container.cards) == 9