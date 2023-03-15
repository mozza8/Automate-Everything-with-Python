import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-20&to=2022-2-21&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
# r = response na request

content = r.json()   # content = python dict

articles = content['articles']


#for article in articles:
   # print('TITLE\n',article['title'], '\nDESCRIPTION\n', article['description'] )

def get_news(topic, from_date, to_date, language='en', api_key='890603a55bfa47048e4490069ebee18c'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    izhodna = open(f'Novice od {from_date} do {to_date}', mode='w', encoding='utf-8')
    for article in articles:
        print(article)
        a = (f"TITLE\n {article['title']}  \nDESCRIPTION\n {article['description']}\n\n")
        izhodna.write(a)
    return results

print(get_news(topic='space', from_date='2023-2-17', to_date='2023-2-20'))
