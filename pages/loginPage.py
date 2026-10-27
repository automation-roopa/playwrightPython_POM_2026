from playwright.sync_api import Page


class LoginPage:
    URL = "https://oreo.sheepa.in/login"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.email_input = page.get_by_placeholder("Enter email")
        self.password_input = page.get_by_placeholder("Enter password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self) -> None:
        self.page.goto(self.URL)

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()