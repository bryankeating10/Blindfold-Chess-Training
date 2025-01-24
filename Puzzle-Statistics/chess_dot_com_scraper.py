# Combines the puzzle data from multiple pages on my Chess.com
# account and formats it into a table in Excel

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Optional: Run in headless mode (no GUI)
driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)

try:
    # Open Chess.com login page
    driver.get("https://www.chess.com/login")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Locate the login elements (username and password fields)
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter your Chess.com credentials
    username_field.send_keys("BKChessMaster2")  # Replace with your Chess.com username
    password_field.send_keys("chesspasshaha12A")  # Replace with your Chess.com password

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for successful login (check if the page URL changes or a specific element appears)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.profile-avatar"))
    )

    # Now that we're logged in, navigate to the puzzles page
    driver.get("https://www.chess.com/puzzles/problems?page=20")

    # Wait for the puzzle table to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "puzzle-list"))
    )

    # Extract data from the puzzle table
    puzzles = driver.find_elements(By.CSS_SELECTOR, ".puzzle-list .puzzle-item")

    # Print the puzzle details
    for puzzle in puzzles:
        puzzle_title = puzzle.find_element(By.CSS_SELECTOR, ".puzzle-title").text
        puzzle_rating = puzzle.find_element(By.CSS_SELECTOR, ".rating").text
        print(f"Title: {puzzle_title}, Rating: {puzzle_rating}")

finally:
    # Clean up and close the browser
    driver.quit()
