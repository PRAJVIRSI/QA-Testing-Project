from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_product_search():
    driver_path = r"C:\Study\SEM4\WSQA\chromedriver-win64\chromedriver.exe"  
    
    try:
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        
        driver.get("https://www.amazon.ca/")
        print("Navigated to Amazon.ca")
        
          # Pause to observe results
        input("Press Enter to continue and close the browser...")
        
        # Find the search box and enter the search term
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)
        print("Entered search term and submitted")
        
        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        print("Search results loaded")
        
        # Apply Brand Filter (Asus)
        brand_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Asus']"))
        )
        brand_filter.click()
        print("Clicked on Asus brand filter")
        time.sleep(2)  # Wait for the filter to apply
        
        # Apply Operating System Filter (Windows 11 Home)
        os_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Windows 11 Home']"))
        )
        os_filter.click()
        print("Clicked on Windows 11 Home filter")
        time.sleep(2)  # Wait for the filter to apply
        
        # Verify results
        results = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
        assert len(results) > 0, "No search results found"
        print(f"Test passed: {len(results)} results found.")
        
         # Pause to observe results
        input("Press Enter to continue and close the browser...")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if 'driver' in locals():
            driver.quit()

# Run the test
test_product_search()
