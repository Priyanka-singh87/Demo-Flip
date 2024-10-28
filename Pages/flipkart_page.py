# pages/flipkart_page.py
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlipkartPage:

    title_laptop = "(//div[@class='KzDlHZ'])[1]"
    title_laptop = "//span[contains(text(),'CHUWI Intel Celeron Dual Core')]"



    def __init__(self, driver):
        self.driver = driver



    def close_login_popup(self):
        try:
            close_button = self.driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
            close_button.click()
        except Exception as e:
            print("Login popup not found or could not be closed:", e)

    def search_product(self, product_name):
        search_box = self.driver.find_element(By.NAME, 'q')  # Adjust if necessary
        search_box.clear()  # Clear any existing text
        search_box.send_keys(product_name)
        search_box.submit()


    # def get_product_titles(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_all_elements_located((By.XPATH, "//div[@class='_4rR01T']"))
    #     )
    #     return self.driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")

    def get_product_titles(self):
        try:
            # Wait for either products to load or an indication that no results were found
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'No results found')]"))
                # Adjust the XPath based on actual no-results text
            )
            # Check if products are available
            titles = self.driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
            return titles
        except TimeoutException:
            # If no results found element is not present, return an empty list
            return []

    # def add_to_cart(self, index):
    #     product = self.driver.find_elements(By.XPATH, "(//div[@class='KzDlHZ'])[1]")
    #     product.click()
    #     add_to_cart_button = self.driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    #     add_to_cart_button.click()

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


