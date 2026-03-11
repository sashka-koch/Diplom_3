from pages.order_feed_page import OrderFeedPage
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://stellarburgers.education-services.ru/"


def test_total_completed_increases(driver):

    page = OrderFeedPage(driver)

    page.open_order_feed()

    initial_total = page.get_total_done()

    driver.get(BASE_URL)

    page.create_order()

    driver.get(BASE_URL + "feed")

    WebDriverWait(driver, 10).until(
        lambda d: page.get_total_done() > initial_total
    )

    assert page.get_total_done() > initial_total


def test_today_completed_increases(driver):

    page = OrderFeedPage(driver)

    page.open_order_feed()

    initial_today = page.get_today_done()

    driver.get(BASE_URL)

    page.create_order()

    driver.get(BASE_URL + "feed")

    WebDriverWait(driver, 10).until(
        lambda d: page.get_today_done() > initial_today
    )

    assert page.get_today_done() > initial_today


def test_order_appears_in_progress(driver):

    page = OrderFeedPage(driver)

    order_number = page.create_order()

    driver.get(BASE_URL + "feed")

    WebDriverWait(driver, 10).until(
        lambda d: page.order_is_in_progress(order_number)
    )

    assert page.order_is_in_progress(order_number)