import sys
sys.path.append(sys.path[0] + "/..")

from setup.setup import Setting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



set_up = Setting()

class Selectors:
    item = "//img[@title='Apple Cinema 30{}']".format('"')
    wish_list = "wishlist-42"
    product_actions = "product-action"
    url = "https://ecommerce-playground.lambdatest.io/"
    action = ActionChains(set_up.driver)
    

class TestBuy(Selectors):    
    def test_add_item_to_wish_list(self):
        set_up.setUp()
        set_up.driver.get(self.url)
        product_action_pop_up = set_up.driver.find_element(By.CLASS_NAME, self.product_actions)
        item = set_up.driver.find_element(By.XPATH, self.item)

        #Use JS to scroll product into view:
        set_up.driver.execute_script("arguments[0].scrollIntoView();", item)

        #Use the ActionChains to hover over the target product:
        self.action.move_to_element(item).perform()

        #Scroll parent action button into view:
        set_up.driver.execute_script("arguments[0].scrollIntoView();", product_action_pop_up)

        #hover over the actions button:
        self.action.move_to_element(product_action_pop_up).perform()

        #Wait for element visibility:
        WebDriverWait(set_up.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.wish_list)))
        wish_list = set_up.driver.find_element(By.CLASS_NAME, self.wish_list)
        
        #Check is element is visible and active
        assert wish_list.is_displayed(), "wishlist element not visible"

        assert wish_list.is_enabled(), "wishlist element is inactive"

        self.action.move_to_element(wish_list).perform()
        
        print(wish_list.is_displayed())

        print("Enabled", wish_list.is_enabled())

        #Use JavaScript to click element since the target is dynamic
        set_up.driver.execute_script("arguments[0].click();", wish_list)

        set_up.driver.implicitly_wait(10)

        set_up.tearDown()