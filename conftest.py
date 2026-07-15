import os
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
SCREENSHOT_DIR = ROOT / "screenshots"
REPORT_DIR = ROOT / "reports"

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser: chromium, firefox, webkit"
    )

@pytest.fixture
def browser(playwright_instance, request):

    browser_name = request.config.getoption("--browser")

    browser = getattr(playwright_instance, browser_name).launch(
        headless=False
    )

    context = browser.new_context()

    yield context

    context.close()
    browser.close()
    
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1440, "height": 900},
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def browser(playwright_instance, browser_context_args):
    browser = playwright_instance.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context(**browser_context_args)
    yield context
    context.close()
    browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        SCREENSHOT_DIR.mkdir(exist_ok=True)
        screenshot_path = SCREENSHOT_DIR / f"{item.nodeid.replace('::', '_')}.png"
        page = item.funcargs.get("page")
        if page is not None:
            page.screenshot(path=str(screenshot_path), full_page=True)
