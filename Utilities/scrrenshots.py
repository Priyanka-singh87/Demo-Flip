import os
import time
from selenium.webdriver.common.by import By

def capture_screenshot(driver, test_name):
    # Create a directory for failed screenshots if it doesn't exist
    screenshot_dir = "failed_screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Generate a unique filename using the test name and current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_file = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

    # Save the screenshot
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved to: {screenshot_file}")
