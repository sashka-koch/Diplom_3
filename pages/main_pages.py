import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage


class MainPage(BasePage):

    constructor_button = (By.XPATH, "//p[text()='Конструктор']")
    order_feed_button = (By.XPATH, "//a[contains(@href,'/feed')]")
    first_ingredient = (By.CSS_SELECTOR, ".BurgerIngredient")
    constructor_area = (By.CSS_SELECTOR, ".BurgerConstructor")
    ingredient_popup = (By.CSS_SELECTOR, ".Modal_modal")
    close_popup_button = (By.CSS_SELECTOR, ".Modal_modal__close")
    ingredient_counter = (By.CSS_SELECTOR, ".counter_counter__num")

    @allure.step("Клик по кнопке Конструктор")
    def click_constructor(self):
        self.click(self.constructor_button)

    @allure.step("Клик по Лента заказов")
    def click_order_feed(self):
        self.click(self.order_feed_button)

    @allure.step("Открыть ингредиент")
    def click_ingredient(self):
        self.click(self.first_ingredient)

    @allure.step("Закрыть попап ингредиента")
    def close_popup(self):
        self.click(self.close_popup_button)

    @allure.step("Получить значение счетчика")
    def get_counter_value(self):
        text = self.get_text(self.ingredient_counter)
        return int(text) if text else 0

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        ingredient = self.driver.find_element(*self.first_ingredient)
        constructor = self.driver.find_element(*self.constructor_area)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor).perform()

    def is_popup_visible(self):
        return self.is_visible(self.ingredient_popup)