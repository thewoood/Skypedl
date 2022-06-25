from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys


sys.path.insert(0,'/usr/bin/chromedriver')
options = Options()
options.add_argument("ignore-certificate-errors")
options.add_argument("ignore-ssl-errrors")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
prefs = {"download.default_directory" : 'content/skypedl'}
options.add_experimental_option('prefs', prefs)

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


!sudo pip install telegram-upload==0.4.0
!telegram-upload /content/skypedl/Video2.mp4
