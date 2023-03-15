from bs4 import BeautifulSoup
import requests

# Selenium se uporablja za avtomatizacijo v brskalnikih(klikanje, izpolnjevanje, login,..), medtem ko se beautiful soup uporablja za scrapanje podatkov iz brskalnika
# Ne rabiš odpreti brskalnika

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text                  # content je html stran v tekstovni oblik
    soup = BeautifulSoup(content, 'html.parser')      # parse = razčleniti, BeautifulSoup pozna strukturo html-a
    rate = soup.find("span", class_="ccOutputRslt").get_text()  # span element, določen class
    rate = float(rate[:-4])

    return rate

a = input('Name a currency: ').upper()
b = input('Name a currency: ').upper()

current_rate = get_currency(a,b)
print(f'1 {a} is {current_rate} {b}.')