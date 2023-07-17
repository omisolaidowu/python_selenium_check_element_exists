from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

class TestSelection():
    def should_select_text(self):
        drop_down_button = "select-demo"
        selected_value = "selected-value"
        url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"

        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        elements = driver.find_elements(By.ID, drop_down_button)

        assert len(elements)>0, "The element does not exist"
        drop_down = Select(driver.find_element(By.ID, drop_down_button))
        selected = driver.find_element(By.CLASS_NAME, selected_value)
        drop_down.select_by_visible_text("Sunday")
        assert "Sunday" in selected.text, "The expected day not selected"
        
        driver.quit()

should_select_text_from_dropdown = TestSelection()

should_select_text_from_dropdown.should_select_text()