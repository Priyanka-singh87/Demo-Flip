import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.scrrenshots import capture_screenshot

@pytest.fixture(scope='session')
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and in PATH
    driver.implicitly_wait(10)    # Implicit wait
    yield driver
    driver.quit()


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Check if the test failed
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs['driver']  # Access the driver from the test function's arguments
        test_name = item.nodeid.split("::")[-1]  # Get the test function name
        capture_screenshot(driver, test_name)

