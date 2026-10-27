from playwright.sync_api import Page, expect


class ResultsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.results_text = page.get_by_text("Results")

    def validate_results_text_visible(self) -> None:
        expect(self.results_text).to_be_visible()