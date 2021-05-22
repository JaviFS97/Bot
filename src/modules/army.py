from selenium import webdriver
from bs4 import BeautifulSoup

from modules import town

PORRAS = 1
LANCERO = 2
HACHA = 3
EMISARIOS = 4


def recruitTroops(driver, troopType, troopNumber):
    town.clickBuildingSlot(driver, town.BARRACKS)
    
    inputTroop = driver.find_element_by_xpath("//input[@name='t" + str(troopType) + "'][@maxlength='4']")
    inputTroop.send_keys(troopNumber)

    buttonRecruit = driver.find_element_by_xpath("//button[@type='submit']")
    buttonRecruit.click()
    