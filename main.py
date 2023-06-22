import os
import time
import requests
import sys
import config
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import undetected_chromedriver as uc


def is_mac_os():
    return sys.platform == 'darwin'


def find_and_click(driver, xpath):
    while True:
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, xpath).click()
            break
        except:
            pass


def find_and_select(driver, xpath, select_name):
    while True:
        time.sleep(4)
        try:
            Select(driver.find_element(By.XPATH, xpath)).select_by_visible_text(select_name)
            break
        except:
            pass


def send_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Error code: {response.status_code}")


def sleep_random(min=9, max=10):
    time.sleep(randint(min, max))


def check_time_exist(driver, start_time):
    while True:
        if (datetime.now() - start_time).seconds / 60 > 28:
            return False

        find_and_click(driver, "//input[@data-tag0='EU Blue Card / Blaue Karte EU (sect. 18b para. 2)']")
        counter = 0

        while counter != 2:
            time.sleep(1 / 2)
            element = driver.find_element(By.XPATH, "//div[@class='loading']")
            if 'none' in element.get_attribute('style'):
                counter += 1

        has_time = len(driver.find_elements(By.XPATH, "//li[contains(@class, 'errorMessage')]")) == 0
        if has_time:
            find_and_click(driver, "//button[@id='applicationForm:managedForm:proceed']")
            return True
        else:
            type_of_visa_radio = driver.find_element(By.XPATH,
                                                     "//input[@data-tag0='EU Blue Card / Blaue Karte EU (sect. 18b para. 2)']")
            driver.execute_script("arguments[0].checked = false;", type_of_visa_radio)
            time.sleep(1 / 7)


def go_to_select_time():
    driver = uc.Chrome()

    driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")

    find_and_click(driver, "//a[text()='Book Appointment']")
    find_and_click(driver, "//input[@name='gelesen']")
    find_and_click(driver, "//button[@id='applicationForm:managedForm:proceed']")

    find_and_select(driver, "//select[@name='sel_staat']", 'Iran, Islamic Republic')
    find_and_select(driver, "//select[@name='personenAnzahl_normal']", 'one person')
    find_and_select(driver, "//select[@name='lebnBrMitFmly']", 'no')

    find_and_click(driver, "//p[contains(text(), 'Apply for a residence title')]")
    find_and_click(driver, "//p[contains(text(), 'Economic activity')]")

    return driver


while True:
    start = datetime.now()
    driver = go_to_select_time()
    if check_time_exist(driver, start):
        if is_mac_os():
            os.system('osascript -e \'display notification "Found visa time!!!" with title "Visa!" sound name '
                      '"Glass"\'')
        else:
            os.system('notify-send "Timee"')

        try:
            send_message(config.TELEGRAM_API_TOKEN, config.TELEGRAM_CHAT_ID, 'Visa time found!!')
        except:
            pass

        try:
            times = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']//a")
            times[0].click()
        except:
            pass

        while True:
            should_continue = input("Do you want to continue?(Y/N)")
            if should_continue.lower() == 'n':
                exit(0)
            else:
                driver.close()
                break
    else:
        driver.close()
