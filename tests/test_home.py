import pytest
from playwright.sync_api import Page

from pages.homePage import HomePage


@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
def test_dashboard_url_and_title(page: Page, logged_in_page: Page) -> None:
    home = HomePage(page)
    home.validate_dashboard_url()
    home.validate_page_title()


@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
def test_dashboard_url(page: Page, logged_in_page: Page) -> None:
    HomePage(page).validate_dashboard_url()
    