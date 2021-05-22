
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException


def collectReward(driver):
    if isRequestCompleted() == True :
        Mentor = driver.find_element_by_class_name("mentor")
        Mentor.click()

        time.sleep(2)
        for collectButton in driver.find_elements_by_xpath("//div[@class='progress']/button[1]"):
            collectButton.click()


def isRequestCompleted(driver):
    try:
        driver.find_element_by_class_name("bigSpeechBubble")
    except NoSuchElementException:
        return False
    return True

