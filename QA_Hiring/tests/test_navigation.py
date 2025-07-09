from src.pages.sitemap import SitemapPage
from src.pages.homepage import HomePage
from src.config import BASE_URL, HOMEPAGE_URL


def test_site_navigation(driver):
    driver.get(BASE_URL)
    sitemap_page = SitemapPage(driver)

    assert sitemap_page.is_sitemap_loaded(), "Sitemap page did not load properly"

    driver.get(HOMEPAGE_URL)
    home_page=HomePage(driver)
    assert home_page.is_homepage_loaded(), "Home page did not load properly"

    home_page.click_second_destination_card()
    
    assert "destinations/" in home_page.get_current_url_path(), \
        f"URL after clicking card does not contain 'destinations/location'. Current URL: {driver.current_url}"

    assert home_page.is_right_arrow_visible_in_fishing_season(), \
        "Right arrow element not found in Fishing Season section."

    home_page.click_right_arrow()
    print("Clicked on the right arrow.")

    assert home_page.is_new_month_loaded(), "New month element did not load successfully after clicking arrow."
