# ブロック落としゲーム
ここに色々書いていってね！！
# 各自の進捗 
テトリス班

Web班

ランキング班

# お知らせ
テトリス班へ  
https://kusakarism.info/?p=11314  
https://github.com/achiwa912/tet/blob/master/tet.py  
https://chat.openai.com/share/7403bf0e-3eed-4caf-aee6-fc061eda3c13  
import requests  
import json  
server_url = "http://10.1.53.45:5000/receive_data"  
data_to_send = {"得点": score}  
headers = {'Content-Type': 'application/json'}  
response = requests.post(server_url, data=json.dumps(data_to_send), headers=headers)  

http://10.1.53.39:5001/

brew install python-tk  
brew install --cask xquartz  
Pythonを再構築  
pyenv uninstall 3.11.5  
pyenv install 3.11.5  

テトリスのホールド等
https://qiita.com/sekishoku/items/20a88d92bc64b5620d49
https://lets-csharp.com/tetris-cpp-hold/

#使用音源の提供元
https://pixabay.com/ja/music/tetris-theme-korobeiniki-arranged-for-piano-186249/

# 仕様

・テトリスを表示する画面とランキングを表示する画面の2つの画面がある。  
・プログラムを起動するとスタートボタンが表示される。  
・スタートボタンを押すとテトリスがプレイできる画面が表示される。  
・テトリスがプレイできる画面が表示されると自動的にゲームが開始される。  
・長方形のボックスのステージの上部にブロックが出現する。  
・ブロックは十字キー(上以外)とスペースボタンで操作できる。  
・ブロックを右に動かしたい時は十字キーの右を押す。  
・ブロックを左に動かしたい時は十字キーの左を押す。  
・ブロックの落下を加速させたい時は十字キーの下を押す。  
・ブロックを回転させたい時はスペースボタンを押す。  
・ブロックがステージの地面か、積み上がっているブロックに触れると次のブロックがステージの上に出現する。  
・ゲーム中は終了するまでBGMが流れる。  
・ステージの地面に触れていて横一列に隙間なくブロックを並べると、その列が消える。  
・画面の左下に表示されている数字の0は現在のゲームの得点を表している。  
・左下にある得点は、ブロックが消えた時のみ点数が加算される。  
・ブロックの種類は、7種類ありT,J,I,O,L,Z,Sの形をしている。  
・時間経過によって落下しているブロックの落下速度が上昇する。  
・ブロックがステージに入りきらないほど積み上がった場合はゲームが終了する。  
・ゲームが終了した時にスコアをランキング画面に自動的に送信する。  
・


# client/TETRIS.pyの実行
## client/TETRIS.pyの実行に必要なバージョン情報
- Flask==3.0.1
- Requests==2.31.0
- simpleaudio==1.0.4
- Python==3.11.5

## ライブラリの入手
以下のように、pipでインストールします。<br>
```sh
$ pip install flask==3.0.1
$ pip install requests==2.31.0
$ pip install simpleaudio==1.0.4
```

## client/TETRIS.pyを実行する
clientフォルダをダウンロードした後、以下のようにターミナルで実行します。
```sh
$ cd {clientフォルダの場所}/
$ python TETRIS.py
```
画面が表示されたらユーザ名を入力して、提示されたサーバのIPアドレスとポート番号を入力して「ゲーム開始」ボタンを押します。