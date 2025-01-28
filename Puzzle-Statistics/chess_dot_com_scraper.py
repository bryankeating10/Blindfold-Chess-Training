# Combines the puzzle data from multiple pages on my Chess.com
# account and formats it into a table in Excel

# My orginal attempt was to have ChatGPT write the program and I 
# would add to it, but there has been so many issues that I'm going
# to attempt to learn the Selenium package from the ground up and
# build the program myself


# Import Selenium and WebDriver Manager libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome WebDriver and open login page
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.chess.com/login")

# Locate the username and password fields and the login button
username_field = driver.find_element(By.NAME, "Username, Phone, or Email")
password_field = driver.find_element(By.NAME, "Password")
login_button = driver.find_element(By.NAME, "login")

# Enter login credentials
username_field.send_keys("BKChessMaster2")
password_field.send_keys("chesspasshaha12A")

# Click the login button
login_button.click()

# Wait for the page to load
time.sleep(20)
