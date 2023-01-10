from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# define driver as chrome webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# CONSTANTS

# URL from where the tables will be scraped
URL = 'https://pk.indeed.com/jobs?q='
domain = 'supply+chain&l=Karachi'

driver.get(URL+domain)
time.sleep(20)

/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[1]
/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[2]

/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[1]/div
/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[2]/div
/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[17]

/html/body/main/div/div[1]/div/div/div[5]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div[4]