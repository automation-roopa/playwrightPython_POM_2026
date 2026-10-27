from playwright.sync_api import Page, expect


class HomePage:
    URL = "https://oreo.sheepa.in/dashboard"

    def __init__(self, page: Page) -> None:
        self.page = page

    def validate_dashboard_url(self) -> None:
        expect(self.page).to_have_url(self.URL)

    def validate_page_title(self) -> None:
        expect(self.page).to_have_title("ShagunTest")