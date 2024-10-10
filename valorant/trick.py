# from test import WebDriverManager
# import random
# from time import sleep

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

# driver = WebDriverManager.driver


# def rndmDelay(min_delay=2, max_delay=5):
#     """Return a random delay between min_delay and max_delay seconds."""
#     sleep(random.uniform(min_delay, max_delay))

# # Open YouTube
# driver.get('https://www.youtube.com')


# imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

# find element function
def find_element_with_retry(driver, by_locator, max_attempts=3, wait_time=10):
    attempts = 0
    while attempts < max_attempts:
        try:
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(by_locator))
            return element
        except (TimeoutException, StaleElementReferenceException):
            attempts += 1
            print(f'Attempt {attempts} failed. Retrying...')
    print(f'Element with {by_locator} not found after {max_attempts} attempts.')
    raise NoSuchElementException(f'Element with {by_locator} not found after {max_attempts} attempts.')

# get element inner text function
def get_element_inner_text(driver, by_locator):
    element = find_element_with_retry(driver, by_locator)
    return element.text

# =================================================================================================

multileveljd = (By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li[1]/div/div[2]/div/a/div')
singleleveljd = (By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section/div[3]/ul/li[1]/div/div[2]/div/div/div')

useraccname = (By.XPATH, '//*[@id="ember924"]/h1')

for i in range(len(df)):
    driver.get(df['URL'][i])

    UserName = get_element_inner_text(driver, useraccname)
    print(UserName)

    Title = get_element_inner_text(driver, multileveljd)
    if Title==None:
        Title = get_element_inner_text(driver, singleleveljd)
    print(Title)




# //*[@id="ember1796"]/div[1]
# //*[@id="ember729"]/div[1]
# //*[@id="ember1681"]/div[1]


# //*[@id="people-graph-bar-ember1898"]/div/button[1]/div/strong
# //*[@id="people-graph-bar-ember944"]/div/button[1]/div/strong
# //*[@id="people-graph-bar-ember2013"]/div/button[1]/div/strong
# //*[contains(@id, 'people-graph-bar') and contains(@id, 'ember')][1]/div/button[1]/div/strong
# (//*[contains(@id, 'people-graph-bar') and contains(@id, 'ember')][1]/div/button[1]/div/strong)[1]






# //*[@id="profile-content"]/div/div[2]/div/div/main/section[7]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li[1]/div/div[2]/div/a/div
# //*[@id="profile-content"]/div/div[2]/div/div/main/section[5]/div[3]/ul/li[1]/div/div[2]/div[2]/ul/li[1]/div/div[2]/div[1]/a/div
# //*[@id="profile-content"]/div/div[2]/div/div/main/section/div[3]/ul/li[1]/div/div[2]/div/div/div/div/div/div/span[1]
# //*[@id="profile-content"]/div/div[2]/div/div/main/section/div[3]/ul/li[1]/div/div[2]/div/div/div