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
driver.find_element(By.XPATH, "//*[@id='declineAllConsentSummary']").click()
hitta = driver.find_element(By.XPATH, "//*[@id='search']")
hitta.send_keys("3764015")
hitta.send_keys(Keys.ENTER)
time.sleep(8)

def test_checkart():
    nora1 = driver.find_element(By.XPATH, "//*[@id='pdp-content-slot-1']/div[1]/div[7]/div[5]/div/div[4]/div/div[2]")
    nora1 = nora1.text
    assert "1534901" in nora1


