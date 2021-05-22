import os

from selenium import webdriver
from bs4 import BeautifulSoup


def login(driver):
    nameField = driver.find_element_by_name("name")
    nameField.send_keys(os.environ.get("USER"))

    passwordField = driver.find_element_by_name("password")
    passwordField.send_keys(os.environ.get("PASSWORD"))

    loginButton = driver.find_element_by_name("s1")
    loginButton.click()

def logout(driver):
    driver.find_element_by_xpath("//li[@class='logout ']/a").click()
