

from src.util.base import BasePage

from selenium.webdriver.common.by import By


class Watcher(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load_video(self, url):
        '''Load the video'''
        self.driver.get(url)

    def play_video(self):
        button_play = (By.XPATH, '//*[@id="movie_player"]//button[@aria-label="Play"]')
        self.click_button(button_play)

    