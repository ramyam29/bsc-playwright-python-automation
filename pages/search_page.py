from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_BOX = "input[name='q']"
    SEARCH_RESULTS = "//h3"

    def search(self, query: str) -> None:
        self.type_text(self.SEARCH_BOX, query)
        self.page.keyboard.press("Enter")
