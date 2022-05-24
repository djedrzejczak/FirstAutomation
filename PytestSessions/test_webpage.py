from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

wait_time = 10

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://ccc.eu/pl/')
driver.implicitly_wait(10)

def find_element(locator):
    return driver.find_element(*locator)

def find_element_and_click(locator):
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located(locator))
    find_element(locator).click()

def find_element_and_enter_text(locator, text):
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located(locator))
    find_element(locator).clear()
    find_element(locator).send_keys(text)

def press_enter(locator):
    find_element(locator).send_keys(Keys.ENTER)

def close_pop_up(locator):
    find_element(locator).click()

def test_ccc():

    assert driver.title == "Sklep internetowy z butami, odzieżą i akcesoriami - CCC.eu"


    SEARCH_BUTTON = (By.XPATH, "//*[@class='c-menu_icon wf-search']")
    SEARCH_INPUT = (By.XPATH, "//input[@name='search']")
    POPUP_WINDOW = (By.XPATH, "//div[@class='snrs-modal-btn-close close-snrs-modal']")

    find_element_and_click(SEARCH_BUTTON)
    find_element_and_enter_text(SEARCH_INPUT, "tekst do wyszukania")
    time.sleep(3)
    find_element_and_enter_text(SEARCH_INPUT, "buty")
    press_enter(SEARCH_INPUT)
    close_pop_up(POPUP_WINDOW)

    driver.quit()
