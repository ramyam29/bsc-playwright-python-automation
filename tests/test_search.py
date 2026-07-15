import pytest
import re
from playwright.sync_api import expect
from pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.smoke
def test_search_linen(page):
    home = HomePage(page)
    
    # Open homepage
    home.open_homepage()

    # Verify homepage loaded
    # assert "Shirts" in home.get_title()
    expect(page).to_have_title(re.compile("Shirts"))

    # Search for a product
    home.search_product("linen")

    # Verify URL contains search query
    expect(page).to_have_url(re.compile(".*search.*"))
    # assert "linen" in page.url.lower()
    # home.expect_visible(HomePage.SEARCH_INPUT)
    expect(page.locator(HomePage.SEARCH_INPUT)).to_be_visible()