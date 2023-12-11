import pytest

from src.pages.home import HomePage

@pytest.fixture()
def home_page(browser):
  home_page = HomePage(browser)

  home_page.open()

  yield home_page

  home_page.driver.delete_all_cookies()
  home_page.driver.refresh()

def test_home_page_elements(home_page):
  assert home_page.header.is_brand_img_present()
  assert home_page.header.navigation.is_all_nav_categories_visible()
  assert home_page.header.navigation.is_all_nav_categories_clickable()


def test_home_page_card_container(home_page):
  assert home_page.card_container.is_container_present()
  assert home_page.card_container.is_cards_visible()
  assert home_page.card_container.is_cards_clickable()
  assert len(home_page.card_container.cards) == 9

def test_home_page_filters(home_page):
  assert home_page.filters.filters_container.is_displayed()
  
  assert home_page.filters.sort.sort.is_displayed()
  assert len(home_page.filters.sort.sort_options) == 5

  assert home_page.filters.search.search_field.is_displayed()
  assert home_page.filters.search.search_reset_btn.is_displayed()
  assert home_page.filters.search.is_search_reset_btn_clickable()
  assert home_page.filters.search.search_submit_btn.is_displayed()
  assert home_page.filters.search.is_search_submit_btn_clickable()

  assert home_page.filters.price_range_slider.slider.is_displayed()
  assert home_page.filters.price_range_slider.pointer_min.is_displayed()
  assert home_page.filters.price_range_slider.pointer_max.is_displayed()
  assert home_page.filters.price_range_slider.current_min_price.is_displayed()
  assert home_page.filters.price_range_slider.current_min_price.text == "1"
  assert home_page.filters.price_range_slider.current_max_price.is_displayed()
  assert home_page.filters.price_range_slider.current_max_price.text == "100"

def test_home_page_pagination(home_page):
  assert home_page.pagination.is_pagination_present()
  assert not home_page.pagination.is_previous_btn_disabled()
  assert home_page.pagination.is_next_btn_clickable()
  assert len(home_page.pagination.pages) == 3