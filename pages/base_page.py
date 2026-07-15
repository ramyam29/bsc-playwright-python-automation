from typing import Optional
from venv import logger
from utils.logger import get_logger

from playwright.sync_api import Locator, Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def open(self, url: str, wait_until: str = "domcontentloaded") -> None:
        self.logger.info(f"Opening URL : {url}")

        self.page.goto(url, wait_until=wait_until)

    def get_locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str) -> None:
        locator = self.wait_for_visible(selector)
        self.logger.info(f"Clicking {selector}")
        locator.click()

    def type_text(self, selector: str, value: str) -> None:
        locator = self.wait_for_visible(selector)
        logger.info(f"Typing text into {selector}: {value}")
        locator.fill(value)

    def wait_for_visible(self, selector: str, timeout: int = 10000) -> Locator:
        locator = self.get_locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        return locator

    def is_visible(self, selector: str, timeout: int = 10000) -> bool:
        locator = self.get_locator(selector)
        try:
            locator.wait_for(state="visible", timeout=timeout)
            return locator.is_visible()
        except Exception:
            return False

    def press_key(self, key: str) -> None:
        self.logger.info(f"Pressing key: {key}")
        self.page.keyboard.press(key)

    def get_text(self, selector: str) -> str:
        return self.get_locator(selector).inner_text()

    def get_title(self) -> str:
        return self.page.title()

    def take_screenshot(self, path: str, full_page: bool = True) -> None:
        self.logger.info(f"Taking screenshot: {path}")
        self.page.screenshot(path=path, full_page=full_page)

    def wait_for_url(self, url: str, timeout: int = 30000) -> None:
        self.logger.info(f"Waiting for URL: {url}")
        self.page.wait_for_url(url, timeout=timeout)

    def expect_visible(self, selector: str):
        self.logger.info(f"Expecting visibility of {selector}")
        expect(self.get_locator(selector)).to_be_visible()

    def expect_text(self, selector, text):
        self.logger.info(f"Expecting text '{text}' in {selector}")
        expect(self.get_locator(selector)).to_have_text(text)