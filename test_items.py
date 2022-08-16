import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_if_add_to_basket_exists(browser):
    browser.get(link)

#    try:
#        WebDriverWait(browser, 3).until(
#            EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
#        ), "The button was not found"
#    except TimeoutError:
#        print("Failed to find the button")

    assert len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) > 0, "The button was not found"

    # just to verify the language on the button
    time.sleep(30)
