import requests
import json

url="https://game.gtimg.cn/images/lol/act/img/tft/js/chess.js"

r = requests.get(url)
json_str = json.loads(r.content)

for item in json_str['data']:
    print(item)
