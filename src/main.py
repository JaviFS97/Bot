import os
from selenium import webdriver
from dotenv import load_dotenv
from bs4 import BeautifulSoup


from modules import resources, town, army, userManagement, utils


load_dotenv() 

driver = webdriver.Chrome(r"C:\Users\javi-\Desktop\Travian\drivers\chromedriver.exe")
driver.get(os.environ.get("LOGIN_URL"))
driver.maximize_window()


userManagement.login(driver)
utils.closingCookies(driver)
print(resources.getCurrentAmountOfResource(driver, resources.CLAY))
print(resources.getWarehouseCapacity(driver))
print(resources.getGranaryCapacity(driver))
print(resources.getCurrentAmountOfResources(driver))
print(resources.getResourceProduction(driver, resources.CEREAL))
print(resources.getResourcesProduction(driver))
print(resources.getResourceTimeFullIn(driver, resources.CLAY))

# if utils.isThereAnythingBuilding(driver) == False:
#     resources.clickMinLevelOfResource(driver, resources.WOOD)
#     resources.levelUpResourceWithAd(driver)

# print(utils.getTypeOfBuild(driver))
# town.clickTown(driver)
# army.recruitTroops(driver, army.PORRAS, 99)

# userManagement.logout(driver)