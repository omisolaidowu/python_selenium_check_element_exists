import sys
sys.path.append(sys.path[0] + "/..")
from setup.setup import Setting
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

set_up = Setting()

class Selectors:
    item = "//img[@title='Apple Cinema 30{}']".format('"')
    wish_list = "wishlist-42"
    url = "https://ecommerce-playground.lambdatest.io/"
    action = ActionChains(set_up.driver)
    

class TestBuy(Selectors):    
    def test_add_item_to_wish_list(self):
        set_up.setUp()
        set_up.driver.get(self.url)
        
        item = set_up.driver.find_element(By.XPATH, self.item)

        set_up.driver.execute_script("arguments[0].scrollIntoView();", item)
        self.action.move_to_element(item).perform()

        #Check for element visibility:
        element_present = False
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, self.wish_list))(set_up.driver)
        except:
            pass
        assert element_present, "element not found"
        
        wish_list = set_up.driver.find_element(By.CLASS_NAME, self.wish_list)
        
        #Check if element is visible and active
        assert wish_list.is_displayed(), "wishlist element not visible"
        assert wish_list.is_enabled(), "wishlist element is inactive"

        #Use JavaScript to click element since the target is dynamic
        set_up.driver.execute_script("arguments[0].click();", wish_list)

        set_up.tearDown()