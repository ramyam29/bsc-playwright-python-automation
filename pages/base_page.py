from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for_selector(self, selector: str, timeout: int = 10000) -> None:
        self.page.locator(selector).wait_for(timeout=timeout)

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def type_text(self, selector: str, value: str) -> None:
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()
    
    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()
    
    def get_title(self):
        return self.page.title()
    
    def take_screenshot(self, path: str):
        self.page.screenshot(path=path, full_page=True)

    def press_key(self, key: str):
        self.page.keyboard.press(key)
    
    def wait_for_url(self, url):
        self.page.wait_for_url(url)
    
    def get_locator(self, selector):
        return self.page.locator(selector)
    