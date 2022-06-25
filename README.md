# Skypedl
A Selenium-based bot that sign-ins in your skype account and download a video, then upload it to your telegram Saved Messages

#How to use

##How to Download
This bot is desired to work on google colabs, in order to reduce internet traffic consumed by downloading and storing skype videos.
1. First, create a group in skype and choose a unique name for it
2. Every time you try to download a video/presentation, send the desired video to that unique folder.
3. Note that at the moment of running the bot, One and only One video/ presentation should be in that unique group. Meaning, other messages should be deleted and only one message(which is your video) should exist in the chat.
4. After setting up all the parts as shown below, run all the cells in google colab. 
5. It'll ask for your Skype Username and Password.
6. Next, enter the name of that unique folder in which you've sent the video
7. The video should get downloaded. If so, it'll be shown in the Folders of Google Colab.
Note that there's no need to make a group each time you want to download a video. Just delete the previous one(if exists) and send the new one!

#How to Upload
This programm uses Telegram-Upload. Check out its Documentation for more info and configuration.
NOTE: It's recommended to use version 0.4.0 as shown below, since there were some problems with running the latest version (0.5.0).

1. After installing Telgram bot, run the cell to upload the video
2. Enter api_code and api_hash. But wait, what are they?
Go to https://my.telegram.org and enter Api Development Tool. Create a new application with you desired name. Enter www.telegram.org in the website section (if needed)
Note: If you faced an error, you might need to install Opera Mini and create an application using this browser. Thanks to an indian guy who found it :)
3. Once the application is created, copy api_code and api_hash. Enter them when telegram-upload asks.
4. Enter your telegram phone number.
5. Enter the code sent to your telegram account
6. Enter your 2fa password
7. Voila! The video will be uploaded to your telegram saved messages!





#How to setup
1. First install the followings:
```sh
!pip3 install -U selenium
!pip3 install webdriver-manager
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
```

2. Import the followings:
```python
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
```

3. Config the driver:
```python
sys.path.insert(0,'/usr/bin/chromedriver')
options = Options()
options.add_argument("ignore-certificate-errors")
options.add_argument("ignore-ssl-errrors")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
prefs = {"download.default_directory" : 'content/skypedl'}
options.add_experimental_option('prefs', prefs)
```

4. Login to skype and download the video:
```python
driver = webdriver.Chrome('chromedriver', options=options)
url='https://go.skype.com/myaccount'
driver.get(url)

driver.find_element(By.CLASS_NAME,value='ext-text-box').send_keys(input('Skype Email: ')) #email
driver.find_element(By.ID,value='idSIButton9').click() #next
sleep(1)

driver.find_element(By.CLASS_NAME,value='ext-text-box').send_keys(input('Skype Password: ')) #pass
driver.find_element(By.ID,value='idSIButton9').click() #next
sleep(1)

driver.find_element(By.ID,value='idBtn_Back').click() #not signed in
sleep(5)

driver.find_element(By.CSS_SELECTOR,value='._20opP').click()
driver.execute_script('window.scrollTo(0, 1800)')
driver.find_element(By.CSS_SELECTOR,value='.cg-link').click()
sleep(30)

actions = ActionChains(driver=driver)
actions.send_keys(Keys.ENTER).perform()

#reach searchbox
for i in range(6):
    actions.send_keys(Keys.TAB).perform()
    sleep(1)

actions.send_keys(Keys.ENTER).perform()
sleep(1)
actions.send_keys(input('Group Name: ')).perform()

#reach user
for i in range(4):
    actions.send_keys(Keys.TAB).perform()
    sleep(1)

actions.send_keys(Keys.ENTER).perform()
sleep(10)
actions.send_keys(Keys.ENTER).perform()

for i in range(22):
  actions.send_keys(Keys.TAB).perform()
  sleep(1)

actions.send_keys(Keys.ENTER).perform()
sleep(3)

for i in range(3):
  actions.send_keys(Keys.TAB).perform()

actions.send_keys(Keys.ENTER).perform()
sleep(1)
actions.send_keys(Keys.ENTER).perform()


sleep(90) # set it as you wish, meaning as long as you think the dowload process will take time
```

Install Telegram-Upload:
```sh
!sudo pip install telegram-upload==0.4.0
```

Use Telegram-Upload
```sh
!telegram-upload /content/skypedl/Video2.mp4
```
