from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage:

    order_feed_button = (By.XPATH, "//a[contains(@href,'/feed')]")
    create_order_button = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    total_done = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
    today_done = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    order_number = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")

    in_progress_orders = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]//li")

    def __init__(self, driver):
        self.driver = driver

    def open_order_feed(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_feed_button)
        ).click()

    def create_order(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_order_button)
        ).click()

        order_number = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.order_number)
        ).text

        return order_number

    def get_total_done(self):

        total = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_done)
        ).text

        return int(total)

    def get_today_done(self):

        today = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.today_done)
        ).text

        return int(today)

    def order_is_in_progress(self, number):

        orders = self.driver.find_elements(*self.in_progress_orders)

        for order in orders:
            if number in order.text:
                return True

        return False