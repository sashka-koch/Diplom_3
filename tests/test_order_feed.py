import allure
from pages.order_feed_page import OrderFeedPage
from urls.urls import BASE_URL


@allure.feature("Лента заказов")
class TestOrderFeed:


    @allure.title("Увеличивается счетчик выполненных заказов")
    def test_total_completed_increases(self, driver):
        page = OrderFeedPage(driver)

        page.open_order_feed()

        initial_total = page.get_total_done()

        driver.get(BASE_URL)
        page.create_order()

        driver.get(BASE_URL + "feed")

        assert page.get_total_done() > initial_total


    @allure.title("Увеличивается счетчик заказов за сегодня")
    def test_today_completed_increases(self, driver):
        page = OrderFeedPage(driver)

        page.open_order_feed()

        initial_today = page.get_today_done()

        driver.get(BASE_URL)
        page.create_order()

        driver.get(BASE_URL + "feed")

        assert page.get_today_done() > initial_today


    @allure.title("Заказ появляется в работе")
    def test_order_appears_in_progress(self, driver):
        page = OrderFeedPage(driver)

        order_number = page.create_order()

        driver.get(BASE_URL + "feed")

        assert page.order_is_in_progress(order_number)