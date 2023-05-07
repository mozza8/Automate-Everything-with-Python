from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # importaš tipke
import time
from datetime import datetime


# Naloga  =  Scrapaj podatek in ga shrani v datoteko, katere ime je trenutni datum in čas

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
    output = float(text.split(":")[1])
    return (output)


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    time.sleep(2)
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        ime = f'{dt_string}.txt'
        izhodna = open(ime, mode='w', encoding='utf-8')
        izhodna.write(str(clean_text(element.text)))
        time.sleep(2)




print(main())


