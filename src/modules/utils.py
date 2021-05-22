
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import *

from modules import resources


RESOURCE = "RESOURCE"
BUILDINGS = "BUILDINGS"
NOTHING_BUILDING = "NOTHING_BUILDING"


def closingCookies(driver):
    cookies = driver.find_element_by_class_name("cmpboxbtn")
    cookies.click()

def isThereAnythingBuilding(driver):
    try:
        driver.find_element_by_class_name("buildingList")
    except NoSuchElementException:
        return False
    return True

def getTypeOfBuild(driver):

    if isThereAnythingBuilding(driver) == False:
        return NOTHING_BUILDING

    buildingList = driver.find_element_by_class_name("buildingList")
    buildingListHtml = BeautifulSoup(buildingList.get_attribute("innerHTML"), 'html.parser')

    liList = buildingListHtml.find_all('li')
    originalText = liList[0].div.get_text()
    procesedText = originalText.split('Nivel')[0].strip()
    if (procesedText == resources.MINA_DE_HIERRO or procesedText == resources.LEÑADOR or procesedText == resources.BARRERA or procesedText == resources.GRANJA):
        return RESOURCE
    return BUILDINGS
