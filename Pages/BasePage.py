import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class BasePage:

    LONG_WAIT = 30
    MEDIUM_WAIT = 15
    SMALL_WAIT = 10
    VERY_SMALL_WAIT = 5



    def __init__(self, driver):
        self.driver = driver


    def get_element(self, locator="", by_type=""):
        element = None
        if by_type == "id":
            element = self.driver.find_element("id",locator)
        elif by_type == "name":
            element = self.driver.find_element("name",locator)
        elif by_type == "css":
            element = self.driver.find_element("css",locator)
        elif by_type == "xpath":
            element = self.driver.find_element("xpath",locator)
        elif by_type == "classname":
            element = self.driver.find_element("classname",locator)
        return element

    def get_element_type(self, by_type=""):
        element_type = None
        if by_type.lower() == "css":
            element_type = By.CSS_SELECTOR
        elif by_type.lower() == "xpath":
            element_type = By.XPATH
        elif by_type.lower() == "id":
            element_type = By.ID
        elif by_type.lower() == "name":
            element_type = By.NAME
        elif by_type.lower() == "classname":
            element_type = By.CLASS_NAME
        return element_type

    def scroll_to_element(self, locator, by_type):
        element = self.get_element(locator, by_type)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_click_element(self, locator, by_type):
        element = self.get_element(locator, by_type)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def wait_till_element_present(self, locator="", by_type=""):
        element_type = self.get_element_type(by_type)
        element=WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.presence_of_element_located((element_type, locator))
        )
        return element.is_displayed()


    def wait_till_element_not_present(self, locator="", by_type=""):
        element_type = self.get_element_type(by_type)
        WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.invisibility_of_element_located((element_type, locator))
        )


    def wait_till_element_visible(self, locator="", by_type=""):
        element_type = self.get_element_type(by_type)
        WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.visibility_of_element_located((element_type, locator))
        )

    def wait_till_element_invisible(self, locator="", by_type=""):
        element_type = self.get_element_type(by_type)
        WebDriverWait(self.driver, self.LONG_WAIT).until(
            EC.invisibility_of_element_located((element_type, locator))
        )

    def get_text(self, locator="", by_type=""):
        element = self.get_element(locator, by_type)
        return element.text

    def clear_text_field(self, locator="", by_type=""):
        element = self.get_element(locator, by_type)
        element.clear()

    def sendKeys(self, locator="", by_type="", input_text=""):
        self.wait_till_element_visible(locator, by_type)
        element = self.get_element(locator, by_type)
        element.send_keys(input_text)

    def mouse_over_to_element(self, locator="", by_type=""):
        element = self.get_element(locator, by_type)
        mouse_hover = ActionChains(self.driver).move_to_element(element)
        mouse_hover.perform()

    def wait_till_title_is(self, title=""):
        WebDriverWait(self.driver, self.SMALL_WAIT).until(
            EC.title_is(title)
        )

    def wait_till_title_contains(self, title=""):
        WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.title_contains(title)
        )

    def wait_till_elements_present(self, locator="", by_type=""):
        element_type = self.get_element_type(by_type)
        WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.presence_of_all_elements_located((element_type, locator))
        )

    def wait_till_text_present_in_element(self, locator="", by_type="", text=""):
        element_type = self.get_element_type(by_type)
        WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.text_to_be_present_in_element((element_type, locator), text)
        )

    def wait_till_frame_available_and_switch(self, locator="", by_type=""):
        element_type = self.get_element_type(by_type)
        WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.frame_to_be_available_and_switch_to_it((element_type, locator))
        )

    def wait_till_element_is_clickable(self, locator="", by_type=""):
        element_type = self.get_element_type(by_type)
        WebDriverWait(self.driver, self.SMALL_WAIT).until(
            EC.element_to_be_clickable((element_type, locator))
        )

    def wait_till_alert_present(self):
        WebDriverWait(self.driver, self.MEDIUM_WAIT).until(
            EC.alert_is_present()
        )

    def click_element(self, locator, by_type):
        time.sleep(2)
        self.wait_till_element_is_clickable(locator, by_type)
        element = self.get_element(locator, by_type)
        element.click()
        time.sleep(3)

    def click_element_dynamicxpath(self, locator, by_type,dynamicValue,endValue):
        locator=locator+dynamicValue+endValue
        self.wait_till_element_is_clickable(locator, by_type)
        element = self.get_element(locator, by_type)
        element.click()
        time.sleep(8)


    def check_element_dynamicxpath(self,  by_type,dynamicValue,phrase,endValue):
        returnValue=False
        try:
            locator=dynamicValue+phrase+endValue
            self.wait_till_element_is_clickable(locator, by_type)
            element = self.get_element(locator, by_type)
            returnValue=element.is_displayed()
            time.sleep(3)
        except:
            print("Error")
        return returnValue


    def make_element_visible(self, locator, by_type):
        element = self.get_element(locator, by_type)
        self.driver.execute_script("arguments[0].style['visibility'] = 'visible';", element)

    def close_current_tab_focus_primary(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def current_tab_focus_primary(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def checkElementIsVisible(self, locator, by_type):
        value=False
        try:
            self.wait_till_element_visible(locator,by_type)
            element = self.get_element(locator, by_type)
            value= element.is_displayed()
        except:
            value=False
        return value

    def select_values(self,element,value):
        select = Select(element)
        select.select_by_visible_text(value)

    def select_values_from_dropdown(self,dropdown,value):
        manualselect = self.driver.find_element(By.XPATH,dropdown)
        select = Select(manualselect)
        select.select_by_value(value)


























