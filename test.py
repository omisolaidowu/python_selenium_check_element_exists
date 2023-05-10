import sys
sys.path.append(sys.path[0] + "/..")

from setup.setup import Setting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class Selectors:
    drop_down_button = "select-demo"
    alt_element = "options-demo"


set_up = Setting()
url = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"

set_up.setUp()

set_up.driver.get(url)

drop_down_element = set_up.driver.find_element(By.ID, "select-demo")

global element2

try:
    element2 = set_up.driver.find_element(By.CLASS_NAME, "select-demo")
except NoSuchElementException:
    print("Element not found")

elem = set_up.driver.find_elements(By.CLASS_NAME, "selectihg-demo")
    

print(drop_down_element is not None)

print(type(elem))



if drop_down_element.is_displayed():
    print(type(drop_down_element))
    drop_down = Select(set_up.driver.find_element(By.ID, "select-demo"))
    drop_down.select_by_visible_text("Sunday")

set_up.tearDown()