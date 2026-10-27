from playwright.sync_api import Locator, Page, expect


class DIDPage:
    URL = "https://oreo.sheepa.in/numbers/default"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.add_did_button = page.get_by_role("button", name="Add DID")
        self.did_input = page.get_by_role("textbox", name="* DID")
        self.country_input = page.get_by_role("combobox", name="* Country")
        self.city_input = page.get_by_role("textbox", name="City")
        self.state_input = page.get_by_role("textbox", name="State")
        self.form: Locator = page.get_by_label("Add a DID")
        self.save_button = page.get_by_role("button", name="Save", exact=True)

    def open(self) -> None:
        self.page.goto(self.URL)

    def open_add_form(self) -> None:
        self.add_did_button.click()

    def fill_form(self, did_number: str, country: str, provider: str) -> None:
        self.did_input.fill(did_number)
        self.country_input.fill(country)
        self.form.get_by_text(country, exact=True).click()
        self.city_input.fill("sddsf")
        self.state_input.fill("sadaf")
        self.page.locator("#add_did_provider_id").click()
        self.form.get_by_text(provider, exact=True).click()
        self.form.get_by_text("YES", exact=True).click()

        values = {
            "add_did_or_includedseconds": "1",
            "add_did_or_cost": "1",
            "add_did_or_init_inc": "01",
            "add_did_or_inc": "01",
            "add_did_or_connectcost": "1",
            "add_did_includedseconds": "01",
            "add_did_cost": "0.01",
            "add_did_init_inc": "01",
            "add_did_inc": "01",
            "add_did_setup": "0.01",
            "add_did_monthlycost": "0.01",
        }
        for field_id, value in values.items():
            self.page.locator(f"#{field_id}").fill(value)

    def save(self) -> None:
        self.save_button.click()
        expect(self.form).not_to_be_visible()
