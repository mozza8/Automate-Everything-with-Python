from selenium import webdriver
import time

token_contract = input('Prilepi token contract: ')

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument(
        "start-maximized")
    options.add_argument(
        "disable-dev-shm-usage")
    options.add_argument(
        "no-sandbox")
    options.add_experimental_option("excludeSwitches", [
        "enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(f"https://etherscan.io/exportData?type=tokentxns&contract={token_contract}&a=&decimal=0")
    return driver



def main():
    driver = get_driver()
    driver_find_element(by='xpath', value='/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click
    time.sleep(5)





url = 'https://etherscan.io/exportData?type=tokentxns&contract=0x2b591e99afe9f32eaa6214f7b7629768c40eeb39&a=&decimal=0'