from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.bombayshirts.com/"

    # TODO: Replace these placeholder selectors with the real locators from the homepage.
    #SEARCH_BUTTON = "TODO: add selector for search trigger"
    SEARCH_BUTTON = ".left_Search"
    #SEARCH_INPUT = "TODO: add selector for search input"
    #SEARCH_SUBMIT = "TODO: add selector for search submit action"
    SEARCH_INPUT = "#stDesktopSearchBox input[name='st']"

    def open_homepage(self) -> None:
        self.open(self.URL)

    def click_search(self) -> None:
        self.click(self.SEARCH_BUTTON)

    def search_product(self, product_name: str) -> None:
        self.click(self.SEARCH_BUTTON)
        self.type_text(self.SEARCH_INPUT, product_name)
        self.page.keyboard.press("Enter")

    def get_title(self) -> str:
        return super().get_title()
