import os

from selenium import webdriver
from bs4 import BeautifulSoup

BARRACKS = "Cuartel"


def clickBuildingSlot(driver, buildingName):
    villageMap = driver.find_element_by_id("village_map")
    villageMapListHtml = BeautifulSoup(villageMap.get_attribute("innerHTML"), 'html.parser')
    for div in villageMapListHtml.findAll('div'):
        dataName = div.get("data-name")
        if dataName == buildingName:
            print(div)
            print(div.a['href'])
            driver.get(os.environ.get("COMMON_URL") + div.a['href'])

def clickTown(driver):
    driver.get(os.environ.get("COMMON_URL") + "dorf2.php")
