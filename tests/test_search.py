import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage


@pytest.mark.ui
@pytest.mark.smoke
def test_search_linen(page):
    home = HomePage(page)
    
    # Open homepage
    home.open_homepage()

    # Verify homepage loaded
    assert "Shirts" in home.get_title()

    # Search for a product
    home.search_product("linen")

    # Verify URL contains search query
    assert "linen" in page.url.lower()