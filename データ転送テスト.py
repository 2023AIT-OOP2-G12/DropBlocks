import requests
import json

# サーバーのIPアドレスをaddressに、ポート番号をportに入れてください
address = "10.1.53.20"
port = "5001"
# 送りたいスコアをscoreに入れる
score = 2000

#以下は指定されたサーバーに指定したスコアを送信します。
server_url = "http://"+address+":"+port+"/receive_data"
data_to_send = {"得点": score}
headers = {'Content-Type': 'application/json'}
response = requests.post(server_url, data=json.dumps(data_to_send), headers=headers)