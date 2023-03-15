from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.buzzerbeater.com/login.aspx?timeout=yes&sstart=yes")
    return driver


def main():
    driver = get_driver()
    driver.find_element(by='id', value='cphContent_txtUserName').send_keys('moza8')
    driver.find_element(by='id', value='cphContent_txtPassword').send_keys('deeppurple8' + Keys.RETURN)
    time.sleep(5)
    # ni več imena tam kt je blu zatu tukaj vrže error
    driver.find_element(by='xpath',
                        value='/html/body/div[2]/form/div[5]/div/div[4]/div[6]/div[2]/table/tbody/tr[2]/td[3]/a/img').click()
    time.sleep(3)
    driver.find_element(by='id', value='cphContent_tbSubject').send_keys('Zdravo')
    time.sleep(2)
    driver.find_element(by='id', value='cphContent_tbMessage').send_keys(
        'Tukaj računalnik tvojega brata. Hoče, da ti povem, da pejt spat.')
    time.sleep(3)
    # driver.find_element(by='id', value="cphContent_btnSend").click()
    time.sleep(5)
    print(driver.current_url)


main()