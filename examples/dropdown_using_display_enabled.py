from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

class TestSelection():
    def should_select_text(self):
          
        drop_down_button = "select-demo"
        selected_value = "selected-value"
        url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"

        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        element_present = False
        try:
            target_element = driver.find_element(By.ID, drop_down_button)
            element_present = EC.presence_of_element_located((By.ID, drop_down_button))(self.driver)
        except:
            pass
        assert element_present, "element not found"

        assert target_element.is_displayed(), "The element is not visible"
        assert target_element.is_enabled(), "Element is visible but disabled"

        drop_down = Select(target_element)
        selected = driver.find_element(By.CLASS_NAME, selected_value)
        drop_down.select_by_visible_text("Sunday")

        assert "Sunday" in selected.text, "The expected day not selected"
        print(f"selected text: {selected.text}, Test status: Passed")
        
        driver.quit()
        
should_select_text_from_dropdown = TestSelection()

should_select_text_from_dropdown.should_select_text()