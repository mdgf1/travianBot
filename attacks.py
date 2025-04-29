from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import random
import traceback

def random_sleep():
    time_to_sleep = random.uniform(0.5, 0.75)
    time.sleep(time_to_sleep)

def attack_oasis(driver, config_values):
    actionChains = ActionChains(driver)
    oasis = []
    for _ in range(len(config_values["oasis"])):
        random_sleep()

        x, y = config_values["oasis"].pop(0)

        driver.find_element(By.CSS_SELECTOR, "a.map").click()
        x_elem = driver.find_element(By.ID, "xCoordInputMap")
        x_elem.clear()
        actionChains.double_click(x_elem).perform()
        x_elem.send_keys(str(x))
        random_sleep()

        y_elem = driver.find_element(By.ID, "yCoordInputMap")
        y_elem.clear()
        actionChains.double_click(y_elem).perform()
        y_elem.send_keys(str(y))
        random_sleep()

        driver.find_element(By.XPATH, "//form[@id='mapCoordEnter']//button[normalize-space(text())='OK']").click()
        random_sleep()

        map_el = driver.find_element(By.CSS_SELECTOR, ".contentContainer")
        click_element_center(driver, map_el)
        random_sleep()

        try:
            driver.find_element(By.XPATH, "//table[@id='troop_info']//td[normalize-space(text())='none']")
        except Exception:
            print(traceback.format_exc())
            oasis.insert(0, (x, y))
            continue

        random_sleep()
        
        try:
            try:
                driver.find_element(By.CSS_SELECTOR, "div.option:nth-child(3)").click()
            except Exception:
                driver.find_element(By.CSS_SELECTOR, "div.options:nth-child(1) > div:nth-child(2) > a:nth-child(1)").click()
                    
        except Exception:
            print(traceback.format_exc())
            oasis.insert(0, (x, y))
            continue
        random_sleep()

        try:
            max_troops = driver.find_element(By.CSS_SELECTOR, 'a[onclick*="troop[t1]"]').text                
            max_troops = max_troops.replace('\u202d', '')
            max_troops = max_troops.replace('\u202c', '')
            if int(max_troops) >= int(config_values["min_troops_a"]):
                legionaires_input = driver.find_element(By.CSS_SELECTOR, "td.line-first:nth-child(1) > input:nth-child(2)")
                legionaires_input.send_keys(config_values["min_troops_a"])
            else:
                max_troops = driver.find_element(By.CSS_SELECTOR, 'a[onclick*="troop[t5]"]').text
                max_troops = max_troops.replace('\u202d', '')
                max_troops = max_troops.replace('\u202c', '')
                if int(max_troops) >= int(config_values["min_troops_b"]):
                    hourse_input = driver.find_element(By.CSS_SELECTOR, "#troops > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(2)")
                    hourse_input.send_keys(config_values["min_troops_b"])
                else:
                    oasis.insert(0, (x, y))
                    oasis.extend(config_values["oasis"])
                    break
        except Exception:
            try:
                max_troops = driver.find_element(By.CSS_SELECTOR, 'a[onclick*="troop[t5]"]').text
                max_troops = max_troops.replace('\u202d', '')
                max_troops = max_troops.replace('\u202c', '')
                if int(max_troops) >= int(config_values["min_troops_b"]):
                    hourse_input = driver.find_element(By.CSS_SELECTOR, "#troops > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(2)")
                    hourse_input.send_keys(config_values["min_troops_b"])
                else:
                    oasis.insert(0, (x, y))
                    oasis.extend(config_values["oasis"])
                    break
            except Exception:
                print(traceback.format_exc())
                oasis.insert(0, (x, y))
                oasis.extend(config_values["oasis"])
                break

        random_sleep()
        try:
            driver.find_element(By.XPATH, "//button[normalize-space(text())='Send']").click()
        except Exception:
            print(traceback.format_exc())
            oasis.insert(0, (x, y))
            continue
        random_sleep()
        try:
            driver.find_element(By.XPATH, "//button[normalize-space(text())='Confirm']").click()
        except Exception:
            print(traceback.format_exc())
            oasis.insert(0, (x, y))
            continue
        oasis.append((x, y))

    config_values["oasis"] = oasis
    driver.find_element(By.CSS_SELECTOR, "a.village:nth-child(1)").click()

def attack_natares(driver, config_values):
    actionChains = ActionChains(driver)
    natares = []
    for _ in range(len(config_values["natares"])):
        random_sleep()

        x, y = config_values["natares"].pop(0)

        driver.find_element(By.CSS_SELECTOR, "a.map").click()
        x_elem = driver.find_element(By.ID, "xCoordInputMap")
        x_elem.clear()
        actionChains.double_click(x_elem).perform()
        x_elem.send_keys(str(x))
        random_sleep()

        y_elem = driver.find_element(By.ID, "yCoordInputMap")
        y_elem.clear()
        actionChains.double_click(y_elem).perform()
        y_elem.send_keys(str(y))
        random_sleep()

        driver.find_element(By.XPATH, "//form[@id='mapCoordEnter']//button[normalize-space(text())='OK']").click()
        random_sleep()

        map_el = driver.find_element(By.CSS_SELECTOR, ".contentContainer")
        click_element_center(driver, map_el)
        random_sleep()
        
        try:
            driver.find_element(By.CSS_SELECTOR, "div.options:nth-child(1) > div:nth-child(3) > a:nth-child(1)").click()
        except Exception:
            print(traceback.format_exc())
            natares.insert(0, (x, y))
            continue
        random_sleep()

        try:
            max_troops = driver.find_element(By.CSS_SELECTOR, 'a[onclick*="troop[t1]"]').text                
            max_troops = max_troops.replace('\u202d', '')
            max_troops = max_troops.replace('\u202c', '')
            if int(max_troops) >= int(config_values["min_troops_a"]):
                legionaires_input = driver.find_element(By.CSS_SELECTOR, "td.line-first:nth-child(1) > input:nth-child(2)")
                legionaires_input.send_keys(config_values["min_troops_a"])
            else:
                max_troops = driver.find_element(By.CSS_SELECTOR, 'a[onclick*="troop[t5]"]').text
                max_troops = max_troops.replace('\u202d', '')
                max_troops = max_troops.replace('\u202c', '')
                if int(max_troops) >= int(config_values["min_troops_b"]):
                    hourse_input = driver.find_element(By.CSS_SELECTOR, "#troops > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(2)")
                    hourse_input.send_keys(config_values["min_troops_b"])
                else:
                    natares.insert(0, (x, y))
                    natares.extend(config_values["natares"])
                    break
        except Exception:
            try:
                max_troops = driver.find_element(By.CSS_SELECTOR, 'a[onclick*="troop[t5]"]').text
                max_troops = max_troops.replace('\u202d', '')
                max_troops = max_troops.replace('\u202c', '')
                if int(max_troops) >= int(config_values["min_troops_b"]):
                    hourse_input = driver.find_element(By.CSS_SELECTOR, "#troops > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(2)")
                    hourse_input.send_keys(config_values["min_troops_b"])
                else:
                    natares.insert(0, (x, y))
                    natares.extend(config_values["natares"])
                    break
            except Exception:
                print(traceback.format_exc())
                natares.insert(0, (x, y))
                natares.extend(config_values["natares"])
                break

        random_sleep()
        try:
            driver.find_element(By.XPATH, "//button[normalize-space(text())='Send']").click()
        except Exception:
            print(traceback.format_exc())
            natares.insert(0, (x, y))
            continue
        random_sleep()
        try:
            driver.find_element(By.XPATH, "//button[normalize-space(text())='Confirm']").click()
        except Exception:
            print(traceback.format_exc())
            natares.insert(0, (x, y))
            continue
        natares.append((x, y))

    config_values["natares"] = natares
    driver.find_element(By.CSS_SELECTOR, "a.village:nth-child(1)").click()

        

def click_element_center(driver, element):
    size = element.size
    width, height = size['width'], size['height']
    
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, 0, 0).click().perform()

