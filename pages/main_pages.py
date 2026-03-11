from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MainPage:

    constructor_button = (By.XPATH, "//p[text()='Конструктор']")
    order_feed_button = (By.XPATH, "//a[contains(@href,'/feed')]")

    first_ingredient = (By.XPATH, "(//a[contains(@class,'BurgerIngredient')])[1]")
    ingredient_counter = (By.XPATH, "(//p[contains(@class,'counter')])[1]")

    constructor_area = (By.XPATH, "//section[contains(@class,'BurgerConstructor')]")

    ingredient_popup = (By.XPATH, "//div[contains(@class,'Modal_modal')]")
    close_popup_button = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    def __init__(self, driver):
        self.driver = driver

    def click_constructor(self):
        self.driver.find_element(*self.constructor_button).click()

    def click_order_feed(self):
        self.driver.find_element(*self.order_feed_button).click()

    def click_ingredient(self):
        self.driver.find_element(*self.first_ingredient).click()

    def close_popup(self):
        self.driver.find_element(*self.close_popup_button).click()

    def get_counter_value(self):

        counter = self.driver.find_element(*self.ingredient_counter).text

        if counter == "":
            return 0

        return int(counter)

    def add_ingredient_to_constructor(self):

        ingredient = self.driver.find_element(*self.first_ingredient)
        constructor = self.driver.find_element(*self.constructor_area)

        actions = ActionChains(self.driver)

        actions.drag_and_drop(ingredient, constructor).perform()