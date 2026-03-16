import allure
from pages.main_pages import MainPage


@allure.feature("Конструктор")
class TestConstructor:


    @allure.title("Переход по кнопке Конструктор")
    def test_click_constructor(self, driver):
        page = MainPage(driver)

        page.click_constructor()

        assert "burger" in page.get_current_url()


    @allure.title("Переход в ленту заказов")
    def test_click_order_feed(self, driver):
        page = MainPage(driver)

        page.click_order_feed()

        assert "feed" in page.get_current_url()


    @allure.title("Открытие попапа ингредиента")
    def test_open_ingredient_popup(self, driver):
        page = MainPage(driver)

        page.click_ingredient()

        assert page.is_popup_visible()


    @allure.title("Закрытие попапа ингредиента")
    def test_close_ingredient_popup(self, driver):
        page = MainPage(driver)

        page.click_ingredient()
        page.close_popup()

        assert not page.is_popup_visible()


    @allure.title("Увеличение счетчика ингредиента")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)

        initial = page.get_counter_value()

        page.add_ingredient_to_constructor()

        new_counter = page.get_counter_value()

        assert new_counter > initial