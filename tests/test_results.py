import pytest
from playwright.sync_api import Page, expect

from pages.homePage import HomePage
from pages.resultsPage import ResultsPage


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.results
def test_results_ui(page: Page, logged_in_page: Page) -> None:
    HomePage(page).validate_dashboard_url()
    ResultsPage(page).validate_results_text_visible()
    expect(page).to_have_title("ShagunTest")