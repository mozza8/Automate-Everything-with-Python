import requests
from datetime import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt


ticker = input('Enter the ticker symbol: ')
ticker = ticker.upper()

from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

# string pretvorimo v datetime format--drugi parametr pokaže v kakšni obliki je string
from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

# datetime pretvorimo v epoch format
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


# Če na spletni stran na link , desni klik  in copy address link
url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true'

# ker Yahoo ne dovoljuje scriptom da downloadajo datoteke, s headersom prikažemo, kot da to dela browser
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# contet damo da dobimo no text requests
content = requests.get(url, headers=headers).content
print(type(content))

# uporabimo 'wb' ker delamo z contentom, to je splošni pristop. Če bi delali z textom bi dali 'w'.    'wb' == 'Write-binary'
with open('data.csv', 'wb') as file:
    file.write(content)


df = pd.read_csv('data.csv')

print(df)

df['Date']  = pd.to_datetime(df['Date'])
plt.plot(df.Date, df.Close)
plt.xlabel('Date')

plt.ylabel('Price')
plt.title(ticker)
plt.show()


