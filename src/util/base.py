# pages\\base_pages



import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
# from src.utils.customLogger import LogGen

# logger = LogGen.loggen()

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title
    
    def refresh_page(self):
        self.driver.refresh()

    def find_element_quick(self, by_locator):
        return self.driver.find_element(*by_locator)

    def find_element_with_retry(self, by_locator, max_attempts=3, wait_time=10):
        attempts = 0
        while attempts < max_attempts:
            try:
                element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator))
                return element
            except (TimeoutException, StaleElementReferenceException):
                attempts += 1
        print(f'Element with {by_locator} not found after {max_attempts} attempts.')
        raise NoSuchElementException(f'Element with {by_locator} not found after {max_attempts} attempts.')   
        
    
    def click_button(self, by_locator):
        element = self.find_element_with_retry(by_locator)
        if element.is_enabled():
            element.click()
        else:
            print('button not found')
    
    def do_send_keys(self, by_locator, text):
        element = self.find_element_with_retry(by_locator)
        if element.is_enabled() or element.is_displayed():
            element.send_keys(text)
        else:
            element = self.wait_for_element(by_locator)
            element.send_keys(text)
    
    def clear_input_field(self, by_locator):
        element = self.find_element_with_retry(by_locator)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
    
    def get_element_inner_text(self, by_locator):
        element = self.find_element_with_retry(by_locator)
        return element.text
    
    def is_enabled(self, by_locator):
        '''
        Check if the element is enabled | clickable
        '''
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            if element:
                return True
            else:
                return False
        except TimeoutException:
            print(f'Element with {by_locator} is not enabled.')
            return False

    def is_element_displayed(self, by_locator):
        '''
        Check if the element is displayed
        '''
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            if element:
                return True
        except TimeoutException:
            return False

        return False
    