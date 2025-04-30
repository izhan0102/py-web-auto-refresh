import time
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def monitor_jkbose_results():
   
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized
    
    # Optional: Enable Chrome DevTools Protocol for profiling
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    try:
        # Initialize Chrome driver with appropriate settings for the platform
        if platform.system() == 'Windows':
            # For Windows, specify the cache_valid_range to avoid issues
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        # Navigate to JKBOSE results page
        url = "https://jkbose.nic.in/results/"
        driver.get(url)
        
        print(f"Monitoring {url} - Refreshing every 5 seconds. Press Ctrl+C to stop.")
        
        try:
            while True:
                # Wait for 5 seconds
                time.sleep(5)
                
                # Refresh the page
                driver.refresh()
                print("Page refreshed at:", time.strftime("%H:%M:%S", time.localtime()))
        
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
        finally:
            # Close the browser
            driver.quit()
            
    except Exception as e:
        print(f"Error initializing Chrome driver: {e}")
        print("\nTry running with a simpler initialization:")
        print("1. Make sure Chrome is installed")
        print("2. Try installing chromedriver manually from: https://chromedriver.chromium.org/downloads")

if __name__ == "__main__":
    monitor_jkbose_results() 