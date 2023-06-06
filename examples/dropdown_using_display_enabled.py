from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Setup:
    driver_path = ".../LambdaTest/chromedriver_win32"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

class TestSelection(Setup):
    def should_select_text(self):
          
        drop_down_button = "select-demo"
        selected_value = "selected-value"
        url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url)
        target_element = self.driver.find_element(By.ID, drop_down_button)

        element_present = False
        try:
            element_present = EC.presence_of_element_located((By.ID, drop_down_button))(self.driver)
        except:
            pass
        assert element_present, "element not found"

        assert target_element.is_displayed(), "The element is not visible"
        assert target_element.is_enabled(), "Element is visible but disabled"

        drop_down = Select(target_element)
        selected = self.driver.find_element(By.CLASS_NAME, selected_value)
        drop_down.select_by_visible_text("Sunday")

        assert "Sunday" in selected.text, "The expected day not selected"
        print(selected.text)

        
        
        self.driver.quit()
        
should_select_text_from_dropdown = TestSelection()

should_select_text_from_dropdown.should_select_text()