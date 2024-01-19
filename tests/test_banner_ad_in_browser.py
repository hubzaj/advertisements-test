import pytest
from browser_hz.utils.request import get_request_with_path
from selenium.webdriver.common.by import By
from seleniumwire.request import Request

from network.banner.default import BannerAd
from network.keywords.browser import BrowserKeywords


@pytest.mark.browser
class TestBannerAdInBrowser:

    @pytest.mark.skip
    def test_banner_ad_in_browser(self, browser_keywords: BrowserKeywords) -> None:
        # Given
        ad: BannerAd = BannerAd.REGULAR_AD  # Product of the ad request sent to SSP

        # When
        requests: list[Request] = browser_keywords.display_ad_and_get_network_traffic(
            ad=ad,
            click_locator=(By.ID, ad.get_ad_click_id_locator()),
            requests_paths_to_wait=[
                ad.get_dsp_notification_url(),
                ad.get_click_redirection_url()
            ],
        )

        # Then
        dsp_notification_request: Request = get_request_with_path(requests, path=ad.get_dsp_notification_url())
        assert dsp_notification_request.response is None
        # assert dsp_notification_request.response is not None
        # assert dsp_notification_request.response.status_code == HTTPStatus.OK

    def test_1(self) -> None:
        pass

    def test_2(self) -> None:
        pass
