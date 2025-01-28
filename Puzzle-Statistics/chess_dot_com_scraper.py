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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver and open login page
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.chess.com/login")
print("WebDriver setup complete and login page opened.")

# Wait for the username field to be loaded
wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
try:
    username_field = EC.presence_of_element_located((By.NAME, "Username, Phone, or Email"))
    print("Username field located")
except:
    print("Username field not located")


# Locate the password field
try:
     password_field = EC.presence_of_element_located(By.NAME, "Password")
     print("Password field located")
except:
	print("Password field not located.")

# Locate the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Use XPath to locate the login button
print("Login button located.")

# Enter login credentials
username_field.send_keys("BKChessMaster2")
password_field.send_keys("chesspasshaha12A")
print("Entered login credentials.")

# Click the login button
login_button.click()
print("Login button clicked.")

# Wait for the page to load (you can adjust the time as needed)
time.sleep(5)
print("Waiting for page to load.")

# Optionally, check if login was successful by looking for a specific element after login
# For example, check if the profile icon is present (this is just an example; adjust accordingly)
try:
    profile_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Profile']")))
    print("Login successful!")
except:
    print("Login failed!")

# Optionally, close the browser after testing
# driver.quit()
