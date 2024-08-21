from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_user_registration():
    driver_path = r"C:\Study\SEM4\WSQA\chromedriver-win64\chromedriver.exe" 
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Implicit wait for elements to load

    try:
        # Navigate to Amazon.ca
        driver.get("https://www.amazon.ca/")
        
        # Wait for the CAPTCHA to be solved manually
        input("Please solve the CAPTCHA and press Enter to continue...")
        
        # Hover over the "Account & Lists" to reveal the "Start here" link
        account_lists = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nav-link-accountList"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(account_lists).perform()
        
        # Wait for the "Start here" link to be present and clickable, and then click it
        start_here_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Start here."))
        )
        start_here_link.click()
        
        # Wait for the CAPTCHA to be solved manually
        input("Please solve the CAPTCHA and press Enter to continue...")
        
        # Enter personal details for registration
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "customerName"))
        ).send_keys("Test User")
        
        driver.find_element(By.NAME, "email").send_keys("abc612189@gmail.com")
        
        driver.find_element(By.NAME, "password").send_keys("TestPassword123")
        
        driver.find_element(By.NAME, "passwordCheck").send_keys("TestPassword123")
        
        # Click on "Create your Amazon account" button
        driver.find_element(By.ID, "continue").click()
        
        # Wait for a few seconds to observe the result
        time.sleep(5)
        
        # Wait for the CAPTCHA to be solved manually
        input("Please solve the CAPTCHA and press Enter to continue...")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Script execution finished. Please close the browser manually if it's still open.")

# Run the test
test_user_registration()
