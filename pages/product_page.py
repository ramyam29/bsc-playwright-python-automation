from pages.base_page import BasePage


class ProductPage(BasePage):
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"

    def is_inventory_visible(self) -> bool:
        return self.page.locator(self.INVENTORY_LIST).is_visible()
