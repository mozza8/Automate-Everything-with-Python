import requests
import json

url = "https://graph.facebook.com/v16.0/10225310645446056?fields=link%2Cimages&access_token=EAAKMg5VKvPgBALvJ4ZBVLRjyTpRziOA5dCLXysw8txUvEebqbuDqWL2r5un5lYXozC2DjXgCXMYBpz5ZB7t9XqG3y5rdDZAmxKCbAtwOapdhryZC3C257RKTnfYl32IwacTinGHEXfQ2o9PDHPtWMiddrFZA3a1KtfS6eXFkX7tFvwckImD99A7uDqFJlHSnPYa0R8kIGIj3YZAAuatTlSVu1ZBlunk6WlZCpSzZBA1dCv5TNgc1g0PZCG"
response = requests.get(url)
data = response.text

data = json.loads(data)   # string sptemeni v dict

image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content    # slike so binarne datoteke, ne tekstovne

izhodna = open('image.jpg', 'wb')
izhodna.write(image_bytes)
