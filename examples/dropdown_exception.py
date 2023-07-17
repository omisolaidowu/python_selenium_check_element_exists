from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()

class TestSelection():
    def should_select_text(self):
        try:   
            drop_down_button = "select-demo"
            selected_value = "selected-value"
            url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"

            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get(url)
            target_element = driver.find_element(By.ID, drop_down_button)
            drop_down = Select(target_element)
            selected = driver.find_element(By.CLASS_NAME, selected_value)
            drop_down.select_by_visible_text("Sunday")

            assert "Sunday" in selected.text, "The expected day not selected"
            
            driver.quit()
        except NoSuchElementException as e:
            driver.quit()
            print(e)

should_select_text_from_dropdown = TestSelection()

should_select_text_from_dropdown.should_select_text()