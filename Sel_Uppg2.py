from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'#open rexel website in chrome'
driver.get("https://www.rexel.se")
driver.fullscreen_window()
time.sleep(8)
search = driver.find_element(By.XPATH, "//*[@id='search']")
search.send_keys("3764015")
search.send_keys(Keys.ENTER)
time.sleep(8)

