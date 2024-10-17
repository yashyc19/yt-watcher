# from os import path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from chromedriver_autoinstaller import install

# from config import DevData
# from src.utils.customLogger import LogGen


class WebDriverManager:
    # declare driver at class level
    driver = None
    # logger = LogGen.loggen()

    def __init__(self):
        # initiate driver
        self.init_driver()

    @classmethod
    def init_driver(cls):
        # initialize the driver here
        # logger.info(f'======Loading webdrivers for chrome======')
        options = Options()
        # options.add_argument('--headless')  # headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-gpu')   # disable GPU
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        # prefs = {"download.default_directory": DevData.DOWNLOADS, "download.prompt_for_download": False, "download.directory_upgrade": True, "safebrowsing.enabled": True}
        # options.add_experimental_option("prefs", prefs)

        # get the chromedriver path
        chromedriverpath = install()
        # cls.logger.info(f'chromedriverpath: {chromedriverpath}')
        service = Service(chromedriverpath)

        WebDriverManager.driver = webdriver.Chrome(options=options, service=service) # driver for dev

        # WebDriverManager.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install())) # driver for dev
        WebDriverManager.delete_cache(WebDriverManager.driver)
        WebDriverManager.driver.delete_all_cookies()
        # cls.logger.info('>> Webdriver initiated')
        return WebDriverManager.driver

    @classmethod
    def delete_cache(cls, driver):
        driver.execute_script("window.open('')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get('chrome://settings/clearBrowserData')
        cls.perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    @classmethod
    def perform_actions(cls, driver, keys):
        actions = ActionChains(driver)
        actions.send_keys(keys)
        sleep(1)
        actions.perform()
        # cls.logger.info('======Starting automation======')
    
    @classmethod
    def close_driver(cls):
        # logger.info(f'======Closing webdrivers for chrome======')
        WebDriverManager.driver.close()
        WebDriverManager.driver.quit()
        # cls.logger.info('>> Closing chromedriver ...')