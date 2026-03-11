from pages.main_pages import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_click_constructor(driver):
    page = MainPage(driver)

    page.click_constructor()

    assert "burger" in driver.current_url


def test_click_order_feed(driver):
    page = MainPage(driver)

    page.click_order_feed()

    assert "feed" in driver.current_url


def test_open_ingredient_popup(driver):
    page = MainPage(driver)

    page.click_ingredient()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(page.ingredient_popup)
    )

    popup = driver.find_element(*page.ingredient_popup)

    assert popup.is_displayed()


def test_close_ingredient_popup(driver):
    page = MainPage(driver)

    page.click_ingredient()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(page.ingredient_popup)
    )

    page.close_popup()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(page.ingredient_popup)
    )

    assert True


def test_ingredient_counter_increases(driver):
    page = MainPage(driver)

    initial_counter = page.get_counter_value()

    page.add_ingredient_to_constructor()

    WebDriverWait(driver, 10).until(
        lambda driver: page.get_counter_value() > initial_counter
    )

    new_counter = page.get_counter_value()

    assert new_counter > initial_counter