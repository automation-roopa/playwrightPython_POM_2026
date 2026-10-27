import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.homePage import HomePage
from pages.loginPage import LoginPage

load_dotenv()


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    email = os.getenv("OREO_EMAIL")
    password = os.getenv("OREO_PASSWORD")

    if not email or not password:
        pytest.fail(
            "Set OREO_EMAIL and OREO_PASSWORD in the project .env file or "
            "environment to run authenticated tests."
        )

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(email, password)

    HomePage(page).validate_dashboard_url()
    return page