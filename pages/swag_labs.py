from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException



class SwagLabs(BasePage):

    def exist_icon(self, name_locator):
        try:
            self.find_element(locator=name_locator)
        except NoSuchElementException:
            return False
        return True

    
    
