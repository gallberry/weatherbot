# ライブラリ読み込み
from datetime import datetime
import json
import requests
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# OpenWeatherMap APIコール
payload = {
    'id': 1859730,
    'units': 'metric',
    'lang': 'ja',
    'cnt': 5,
    'appid': '7b55a6c1410fdda11abf1ce9301aeff5'
}
data = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload).json();

# 投稿メッセージ作成
msg_list = ['埼玉県川口市の今後の天気']
for val in data['list']:
    dt = datetime.fromtimestamp(val['dt'])
    msg_list.append(
            '[' + dt.strftime('%Y-%m-%d %H:00') + '] '
            + val['weather'][0]['description'] + ' '
            + str(val['main']['temp_max']) + '℃/' + str(val['main']['temp_min']) + '℃'
    )
msg_list.append('#weather #kawaguchi #openweathermap #saitama #tenki')

# Twitter投稿
twitter = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
msg = '\n'.join(msg_list)
twitter.update_status(status=msg)
print(msg)

