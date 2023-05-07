from selenium import webdriver


# Funkcija ustvari driver in ga vrne
def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  # Odstrani kakšne poop-upe če greš z miško gor--da ne zmede kursorja
    options.add_argument(
        "start-maximized")  # Začne največja velikost brskalnika, ker se lahko vsebina spreminja na velikost zaslona
    options.add_argument(
        "disable-dev-shm-usage")  # Odstrani možnost težave, ki se lahko zgodi, če dostopaš v brskalnik z Linuxa
    options.add_argument(
        "no-sandbox")  # sandbox brskalniki uporabljajo za varnost, z no-sand ima naš script večje privilegije
    options.add_experimental_option("excludeSwitches", [
        "enable-automation"])  # Nekateri strani ne marajo scriptov s tema optionsa se omogoči
    options.add_argument("disable-blink-features=AutomationControlled")

    # spremenljivka driver
    driver = webdriver.Chrome(options=options)  # Chrome class od webdriverja
    driver.get("https://automated.pythonanywhere.com")  # Povezava do spletne strani od kje bo pobiral
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text


print(main())