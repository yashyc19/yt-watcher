# YouTube Watcher

This project is designed to automate the process of opening multiple tabs in a web browser and watching YouTube videos. It uses Selenium WebDriver to manage browser interactions.

## Project Structure
```pycache/ 
.gitignore 
config.json 
Dockerfile 
LICENSE 
README.md 
requirements.txt 
src/ 
    task/ 
        watcher.py 
util/ 
    base.py 
    webdriverManager.py 
    
test.py 
yt-viewer.py
```


## Configuration

The configuration for the project is stored in `config.json`. Below is an example configuration:

```json
{
    "_comment": "time mentioned in seconds | mode: headless or gui | tab_count: number of tabs to open | watch_time: time to watch the video | view_cycles: number of times to watch the video",
    "mode": "headless",
    "url": "https://www.youtube.com/watch?v=RMrVbjhOmeU", 
    "tab_count": 2,
    "watch_time": 5,
    "view_cycles": 3
}
```
- **mode**: setup driver as headless (cli-based | for servers) or gui mode
- **url**: youtube video url
- **tab_count**: number of simultaneous tabs to be used
- **watch_time**: time in seconds to be watched the video for
- **view_cycles**: how many number of time is activity to be done

## Usage
Install Dependencies: Ensure you have all the required dependencies installed. You can install them using:
```
pip install -r requirements.txt
```

Update Configuration: Update the config.json file with the appropriate values.

Run the Script: Execute the main script to start the process:
```
python yt-viewer.py
```

## Files
- yt-viewer.py: Main script to run the YouTube watcher.
- config.json: Configuration file for the project.
- src/util/webdriverManager.py: Manages the WebDriver instance.
- src/task/watcher.py: Contains the logic for watching YouTube videos.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


This [README.md](README.md) file now provides a clear overview of the project, its structure, configuration, and usage instructions.