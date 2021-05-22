from selenium import webdriver
from bs4 import BeautifulSoup

WOOD = "WOOD"
CLAY = "CLAY"
IRON = "IRON"
CEREAL = "CEREAL"

MINA_DE_HIERRO = "Mina de hierro"
LEÑADOR = "Leñador"
GRANJA = "Granja"
BARRERA = "Barrera"


def clickMinLevelOfResource(driver, resource):
    resourceDicc = {
        WOOD: "gid1",
        CLAY: "gid2",
        IRON: "gid3",
        CEREAL: "gid4"
    }
    resourceID = resourceDicc.get(resource)

    minFieldRef = None
    minFieldLevel = 20

    fields = driver.find_elements_by_class_name(resourceID)
    for field in fields:
        fieldHtml = BeautifulSoup(field.get_attribute("innerHTML"), 'html.parser')
        fieldLevel = fieldHtml.div.get_text()
        if int(fieldLevel) < int(minFieldLevel):
            minFieldLevel = fieldLevel
            minFieldRef = field

    minFieldRef.click()

def levelUpResourceWithAd(driver):
    levelUpWithAd = driver.find_element_by_class_name("videoFeatureButton")
    levelUpWithAd.click()

def getCurrentAmountOfResource(driver, resource):
    resourceDicc = {
        WOOD: "l1",
        CLAY: "l2",
        IRON: "l3",
        CEREAL: "l4",
    }
    resourceID = resourceDicc.get(resource)
    resourceType = "granary" if resource == CEREAL else "warehouse"
    
    amountOfResource = driver.find_element_by_xpath("//div[@class='" + resourceType + "']/a/div[@id='" + resourceID + "']")
    return amountOfResource.get_attribute("innerHTML")

def getCurrentAmountOfResources(driver):
    return (getCurrentAmountOfResource(driver, WOOD) + "," +
            getCurrentAmountOfResource(driver, CLAY) + "," +
            getCurrentAmountOfResource(driver, IRON) + "," +
            getCurrentAmountOfResource(driver, CEREAL))


def getWarehouseCapacity(driver):
    warehouseCapacity = driver.find_element_by_xpath("//div[@class='warehouse']/div[@class='capacity']/div[@class='value']")
    warehouseCapacityFormated = warehouseCapacity.get_attribute("innerHTML").replace(".", "").replace("\u202d", "").replace("\u202c", "")
    return warehouseCapacityFormated

def getGranaryCapacity(driver):
    warehouseCapacity = driver.find_element_by_xpath("//div[@class='granary']/div[@class='capacity']/div[@class='value']")
    warehouseCapacityFormated = warehouseCapacity.get_attribute("innerHTML").replace(".", "").replace("\u202d", "").replace("\u202c", "")
    return warehouseCapacityFormated

def getResourceProduction(driver, resource):
    resourcePositionDicc = {
        WOOD: "1",
        CLAY: "2",
        IRON: "3",
        CEREAL: "4",
    }
    resourcePosition = resourcePositionDicc.get(resource)

    resourceProduction = driver.find_element_by_xpath("//table[@id='production']/tbody/tr["+ resourcePosition +"]/td[@class='num']")
    resourceProductionFormated = resourceProduction.get_attribute("innerHTML").strip().replace("\u202d", "").replace("\u202c", "")
    return resourceProductionFormated

def getResourcesProduction(driver):
    return (getResourceProduction(driver, WOOD) + "," +
            getResourceProduction(driver, CLAY) + "," + 
            getResourceProduction(driver, IRON) + "," + 
            getResourceProduction(driver, CEREAL))

def getResourceTimeFullIn(driver, resource):
    timeFullIn = (int(getWarehouseCapacity(driver)) - int(getCurrentAmountOfResource(driver, resource))) / int(getResourceProduction(driver, resource))
    timeFullInSplit = str(timeFullIn).split(".")
    return timeFullInSplit[0] + "h" + str(int(timeFullInSplit[1]) * 60 / 100)[:2] + "min"