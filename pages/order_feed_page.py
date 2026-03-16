import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    order_feed_button = (By.XPATH, "//a[contains(@href,'/feed')]")
    create_order_button = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    total_done = (By.XPATH, "//p[contains(text(),'Выполнено за всё время')]/following-sibling::p")
    today_done = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    order_number = (By.CSS_SELECTOR, ".Modal_modal__title")
    in_progress_orders = (By.CSS_SELECTOR, ".OrderFeed_orderListReady li")

    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        self.click(self.order_feed_button)

    @allure.step("Создать заказ")
    def create_order(self):
        self.click(self.create_order_button)
        return self.get_text(self.order_number)

    @allure.step("Получить количество выполненных заказов")
    def get_total_done(self):
        return int(self.get_text(self.total_done))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_done(self):
        return int(self.get_text(self.today_done))

    def order_is_in_progress(self, number):
        orders = self.driver.find_elements(*self.in_progress_orders)
        for order in orders:
            if number in order.text:
                return True
        return False