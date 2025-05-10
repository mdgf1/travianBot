from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

from attacks import random_sleep

def upgradeLowestResource(driver, resources):
    min_level = float('inf')
    target = None
    for res in resources:
        if "underConstruction" in res.get_attribute("class").split():
            continue
        try:
            level = int(res.find_element(By.CSS_SELECTOR, ".labelLayer").text)
        except Exception:
            res.click()
            random_sleep()
            try:
                btn = driver.find_element(By.CSS_SELECTOR, ".upgradeButtonsContainer .section1 button.build")
                btn.click()
            except NoSuchElementException:
                driver.find_element(By.CSS_SELECTOR, "a.village:nth-child(1)").click()
            return
        if level < min_level:
            min_level = level
            target = res
    target.click()
    random_sleep()
    try:
        btn = driver.find_element(By.CSS_SELECTOR, ".upgradeButtonsContainer .section1 button.build")
        btn.click()
    except NoSuchElementException:
        driver.find_element(By.CSS_SELECTOR, "a.village:nth-child(1)").click()

def getResources(driver):
    resourceField = driver.find_element(By.CSS_SELECTOR, "#resourceFieldContainer")
    resources = resourceField.find_elements(By.TAG_NAME, "a")
    resources = resources[1:]
    return resources

def getResourcesTrees(driver):
    resourceField = driver.find_element(By.CSS_SELECTOR, "#resourceFieldContainer")
    trees = resourceField.find_elements(By.CSS_SELECTOR, "a[data-gid='1']")
    return trees

def getResourcesClays(driver):
    resourceField = driver.find_element(By.CSS_SELECTOR, "#resourceFieldContainer")
    clays = resourceField.find_elements(By.CSS_SELECTOR, "a[data-gid='2']")
    return clays

def getResourcesIrons(driver):
    resourceField = driver.find_element(By.CSS_SELECTOR, "#resourceFieldContainer")
    irons = resourceField.find_elements(By.CSS_SELECTOR, "a[data-gid='3']")
    return irons

def getResourcesCrops(driver):
    resourceField = driver.find_element(By.CSS_SELECTOR, "#resourceFieldContainer")
    crops = resourceField.find_elements(By.CSS_SELECTOR, "a[data-gid='4']")
    return crops

def evolveCrops(driver, value):
    match value:
        case 5:
            resources = getResources(driver)
        case 0 | _:
            return 
    upgradeLowestResource(driver, resources)
    
def evolveMain(driver):
    
    driver.find_element(By.CSS_SELECTOR, "svg.villageCenter > path:nth-child(1)").click()
    random_sleep()
    try:
        center = driver.find_element(By.CSS_SELECTOR, "a.aid26")
        center.click()
        random_sleep()
        btn = driver.find_element(By.CSS_SELECTOR, ".upgradeButtonsContainer .section1 button.build")
        btn.click()
        random_sleep()
        driver.find_element(By.CSS_SELECTOR, "a.village:nth-child(1)").click()

    except NoSuchElementException:
        driver.find_element(By.CSS_SELECTOR, "a.village:nth-child(1)").click()

        

