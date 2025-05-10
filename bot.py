from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time
import threading
import random
import traceback


from config import read_config
from config import EMAIL, PASSWORD
from upgrades import evolveCrops, evolveMain
from attacks import attack_oasis, attack_natares, random_sleep

a_crops = 0
auto_main = False
auto_oasis = False
auto_natares = False
min_seconds = 30
max_seconds = 60

def login(driver, config_values):
    email_text_box = driver.find_element(by=By.CSS_SELECTOR, value="label.input:nth-child(1) > input:nth-child(1)")
    password_text_box = driver.find_element(by=By.CSS_SELECTOR, value="label.input:nth-child(2) > input:nth-child(1)")
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="button.textButtonV2 > div:nth-child(1)")

    print(config_values[EMAIL])
    email_text_box.click()
    email_text_box.send_keys(config_values[EMAIL])

    password_text_box.click()
    password_text_box.send_keys(config_values[PASSWORD])
    login_button.click()

def main():
    opts = Options()
    config_values = read_config()
    if (config_values["windowless"]):
        opts.add_argument("--headless")

    driver = webdriver.Firefox(options=opts)

    driver.get("https://ts8.x1.europe.travian.com/")
    delay = 3
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label.input:nth-child(1) > input:nth-child(1)')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    login(driver, config_values)
    
    while 1:
        try:
            if a_crops != 0:
                try:
                    evolveCrops(driver, a_crops)
                except Exception:
                    print(traceback.format_exc())
                    random_sleep()
                    driver.find_element(by=By.CSS_SELECTOR, value="a.village:nth-child(1)").click()
                    random_sleep()
            if auto_main:
                try:
                    evolveMain(driver)
                except Exception:
                    random_sleep()
                    print(traceback.format_exc())
                    random_sleep()
            if random.choice([True, False]):
                if auto_oasis:
                    try:
                        config_values["oasis"] = attack_oasis(driver, config_values)
                    except Exception:
                        print(traceback.format_exc())
                        random_sleep()
                        driver.find_element(by=By.CSS_SELECTOR, value="a.village:nth-child(1)").click()
                        random_sleep()
                if auto_natares:
                    try:
                        config_values["natares"] = attack_natares(driver, config_values)
                    except Exception:
                        print(traceback.format_exc())
                        random_sleep()
                        driver.find_element(by=By.CSS_SELECTOR, value="a.village:nth-child(1)").click()
                        random_sleep()
            else:
                if auto_natares:
                    try:
                        config_values["natares"] = attack_natares(driver, config_values)
                    except Exception:
                        print(traceback.format_exc())
                        random_sleep()
                        driver.find_element(by=By.CSS_SELECTOR, value="a.village:nth-child(1)").click()
                        random_sleep()
                if auto_oasis:
                    try:
                        config_values["oasis"] = attack_oasis(driver, config_values)
                    except Exception:
                        print(traceback.format_exc())
                        random_sleep()
                        driver.find_element(by=By.CSS_SELECTOR, value="a.village:nth-child(1)").click()
                        random_sleep()

            time.sleep(random.uniform(min_seconds, max_seconds))
        except Exception:
            driver.get("https://ts8.x1.europe.travian.com/dorf1.php")
        


def run_loop():
    print("Commands: crops <int>, main, oasis, natares, status, exit")
    global a_crops, auto_main, auto_oasis, auto_natares
    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue
        parts = user_input.split()
        cmd = parts[0].lower()
        val = parts[1] if len(parts) > 1 else None

        if cmd in ("exit", "quit"):
            print("Goodbye!")
            break
        elif cmd == "status":
            print(
                f"crops={a_crops}, main={auto_main}, "
                f"oasis={auto_oasis}, natares={auto_natares}"
            )
        elif cmd == "crops":
            if val is None:
                print("Usage: crops <integer>")
            else:
                try:
                    a_crops = int(val)
                    print(f"crops = {a_crops}")
                except ValueError:
                    print("Error: value must be an integer.")
        elif cmd == "main":
            auto_main = not auto_main
            print("main =", auto_main)
        elif cmd == "oasis":
            auto_oasis = not auto_oasis
            print("oasis =", auto_oasis)
        elif cmd == "natares":
            auto_natares = not auto_natares
            print("natares =", auto_natares)
        else:
            print("Unknown command. Type 'status' or 'exit'.")




if __name__ == "__main__":
    command_thread = threading.Thread(target=run_loop)
    command_thread.start()

    main()

    command_thread.join()