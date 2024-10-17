# from src.util.webdriverManager import WebDriverManager

# driver = WebDriverManager().driver

# driver.get('https://www.youtube.com/watch?v=RMrVbjhOmeU')

# from time import sleep  
# sleep(50)  # Add a little wait time

# # //*[@id="movie_player"]//button[@aria-label="Play"]


from json import load
from time import sleep
from src.util.webdriverManager import WebDriverManager
from src.task.watcher import Watcher

def get_config():
    """Read configuration file"""

    try:
        with open('default.json', 'r') as file:
            data = load(file)

    except FileNotFoundError:
        with open('config.json', 'r') as file:
            data = load(file)
    
    return data

def init_tabs(driver, tab_count):
    """Opens tabs according to tab amount set in config.json"""

    for _ in range(tab_count - 1):
        driver.execute_script("window.open('about:blank', '_blank');")
        sleep(1)  # Add a little wait time

def load_video(driver, tab_count, url):
    """Open the YouTube link in each tab"""
    
    for tab in range(tab_count):
        driver.switch_to.window(driver.window_handles[tab])
        driver.get(url)
        sleep(1)  # Add a little wait time

def play_video(watcher, tab_count):
    """Click on the play button"""

    for tab in range(tab_count):
        watcher.driver.switch_to.window(watcher.driver.window_handles[tab])
        watcher.play_video()
        sleep(1)
    
def refresh_all(driver, tab_count):
    """Refresh all tabs"""

    for tab in range(tab_count):
        driver.switch_to.window(driver.window_handles[tab])
        driver.refresh()
        sleep(1)  # Add a little wait time

def main():
    """Main Function"""

    print('Initilization')
    config = get_config()

    drivermanager = WebDriverManager()
    driver = drivermanager.driver
    watcher = Watcher(driver)

    print('Opening new tabs')
    init_tabs(driver, config['tab_count'])

    print('Opening links')
    load_video(driver, config['tab_count'], config['url'])

    print('Starting the cycle')
    print('Playing videos')
    print('Press Ctrl+C to exit')

    play_video(watcher, config['tab_count'])

    for cycle in range(config['view_cycles'] - 1):  # -1 because we already played the video once
        print(f'Cycle {cycle + 1}/{config["view_cycles"]}')

        sleep(config['watch_time'])
        refresh_all(driver, config['tab_count'])

        print('Clearing cookies')
        driver.delete_all_cookies()

    print('Exiting...')
    driver.quit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting...')
    except Exception as e:
        print('An error occured:', e)