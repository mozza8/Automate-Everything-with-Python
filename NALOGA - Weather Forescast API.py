import requests

def vremenske_razmere(mesto, api_key='43351154cde5583ff0542471f6542896'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={mesto}&appid={api_key}'
    r = requests.get(url)
    content = r.json()
    obdobja = content['list']
    izhodna = open('data - Weather Forecast', mode='a', encoding='utf-8')
    results = []
    for vreme in obdobja:
        print(vreme)
        tempera = round(int(vreme['main']['temp'])-273.15,1)
        forecast = vreme['weather'][0]['description']
        a = f"{mesto},{vreme['dt_txt']},{tempera},{forecast}\n"
        izhodna.write(a)
    izhodna.close()
    return results

vremenske_razmere(mesto='Ljubljana')