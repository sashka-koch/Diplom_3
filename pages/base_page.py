import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по элементу")
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    @allure.step("Проверка отображения элемента")
    def is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    @allure.step("Ожидание исчезновения элемента")
    def wait_invisible(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url