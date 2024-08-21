from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time  # Import the time module

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        driver_path = r"C:\Study\SEM4\WSQA\chromedriver-win64\chromedriver.exe"  
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)  # Implicit wait for elements to load

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.amazon.ca")
        
         # Pause for manual CAPTCHA solving
        input("Solve the CAPTCHA and press Enter to continue...")
        
        # Wait for the search box to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("laptop")
        driver.find_element(By.ID, "nav-search-submit-button").click()
        
        # Pause for manual CAPTCHA solving
        input("Solve the CAPTCHA and press Enter to continue...")
        
        # Apply Brand Filter (Asus)
        brand_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Asus']"))
        )
        brand_filter.click()
        time.sleep(2)  # Wait for the filter to apply
        
        # Apply Operating System Filter (Windows 11 Home)
        os_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Windows 11 Home']"))
        )
        os_filter.click()
        time.sleep(2)  # Wait for the filter to apply
        
        # Wait for results to load and click on the first item
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-main-slot .s-result-item h2 a"))
        )
        
        # Click the first result
        first_result.click()
        
        # Add to cart
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
        )
        add_to_cart_button.click()
        
        # Handle "No thanks" if it appears
        try:
            no_thanks_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-labelledby='attachSiNoCoverage-announce']"))
            )
            no_thanks_button.click()
        except:
            pass  # If "No thanks" does not appear, continue without interruption
        
        # Verify item added to cart
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".a-size-medium-plus.a-color-base.sw-atc-text"), "Added to Cart")
        )
        self.assertIn("Added to Cart", driver.page_source)
        
        # Pause to observe results
        input("Press Enter to continue and close the browser...")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
