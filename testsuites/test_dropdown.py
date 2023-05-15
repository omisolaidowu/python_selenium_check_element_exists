import sys
sys.path.append(sys.path[0] + "/..")

from setup.setup import Setting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


set_up = Setting()
class Selectors:
    drop_down_button = "select-demo"
    alt_element = "options-demo"
    url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"


class TestDropDown(Selectors):    
    def test_drop_down(self):
        set_up.setUp()

        set_up.driver.get(self.url)

        elements = set_up.driver.find_elements(By.ID, self.drop_down_button)

        single_element = set_up.driver.find_element(By.ID, self.drop_down_button)



        #Using the NoSuchElementException exception:
        try:
            single_drop_down = set_up.driver.find_element(By.CLASS_NAME, self.alt_element)
        except NoSuchElementException:
            print("Element not found")

        
        #Using the is_displayed Boolean
        if single_element.is_displayed():
            drop_down = Select(set_up.driver.find_element(By.ID, self.drop_down_button))
            drop_down.select_by_visible_text("Sunday")
        
    
        #Using elements count
        if len(elements)>0:
            drop_down = Select(set_up.driver.find_element(By.ID, self.drop_down_button))
            drop_down.select_by_visible_text("Sunday")

        set_up.tearDown()