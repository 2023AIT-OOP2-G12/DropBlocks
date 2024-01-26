import requests
import json

# ユーザ名をusernameに入力
username="名無しさん3"
# サーバーのIPアドレスをaddressに、ポート番号をportに入れてください
address = "192.168.3.103"
port = "5001"
# 送りたいスコアをscoreに入れる
score = 3000

#以下は指定されたサーバーに指定したスコアを送信します。
server_url = "http://"+address+":"+port+"/receive_data"
data_to_send = {"ユーザ名":username,"得点": score}
headers = {'Content-Type': 'application/json'}
response = requests.post(server_url, data=json.dumps(data_to_send), headers=headers)