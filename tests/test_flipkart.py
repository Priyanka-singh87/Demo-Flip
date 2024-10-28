# tests/test_flipkart.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.flipkart_page import FlipkartPage

class TestFlipkart:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.flipkart_page = FlipkartPage(driver)
        self.driver.get("https://www.flipkart.com")
        self.flipkart_page.close_login_popup()





    def test_add_product_to_cart(self):
        def add_to_cart(self, index):
            products = self.driver.find_elements(By.XPATH, "(//div[@class='KzDlHZ'])")  # Adjust if necessary

            if len(products) == 0:
                raise Exception("No products available to add to cart.")

            if index < len(products):
                product = products[index]
                product.click()

                # Wait for the add to cart button to be clickable
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='ADD TO CART']"))
                )
                add_to_cart_button = self.driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
                add_to_cart_button.click()
            else:
                raise IndexError("Product index is out of range.")

    def test_invalid_search(self):
        self.flipkart_page.search_product("invalidproduct123")
        #time.sleep(2)  # Wait for results to load
        titles = self.flipkart_page.get_product_titles()
        assert len(titles) == 0, "Products found for invalid search!"

    def test_login_popup_not_displayed(self):
        # This test will simply check if the login popup is closed at the start
        assert not self.driver.find_elements(By.XPATH, "//button[contains(text(), '✕')]")

    def test_multiple_searches(self):
        self.flipkart_page.close_login_popup()  # Close the login popup first
        products = ["Laptops", "Mobile Phones", "Headphones"]
        for product in products:
            self.flipkart_page.search_product(product)
            time.sleep(2)  # Wait for results to load
            self.flipkart_page.search_product(product)

