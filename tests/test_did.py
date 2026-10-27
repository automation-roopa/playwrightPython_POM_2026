import os
import secrets

import pytest
from playwright.sync_api import Page

from pages.didPage import DIDPage


def generate_test_did() -> str:
    return str(secrets.randbelow(900_000_000_000) + 100_000_000_000)


@pytest.mark.did
@pytest.mark.regression
def test_did(logged_in_page: Page) -> None:
    country = os.getenv("OREO_DID_COUNTRY")
    provider = os.getenv("OREO_DID_PROVIDER")
    if not country or not provider:
        pytest.fail(
            "Set OREO_DID_COUNTRY and OREO_DID_PROVIDER in the project .env "
            "file to select the DID country and provider."
        )

    did_number = generate_test_did()
    did_page = DIDPage(logged_in_page)
    did_page.open()
    did_page.open_add_form()
    did_page.fill_form(did_number, country, provider)
    did_page.save()
