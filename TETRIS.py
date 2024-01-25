#################### Rough TETRIS ####################
import requests
import json
import tkinter as tk
import random
from tkinter import messagebox
import simpleaudio as sa #simpleaudioのインストールが必要
import threading

#################### サーバーを指定する ####################
# サーバーのIPアドレスをip_addressに入力してください
ip_address = "10.1.53.45"
# サーバーのポート番号をport_numberに入力してください。
port_number = "5001"

global play_obj  # グローバル変数として宣言

SIZE = 30       #ブロックのサイズ
moveX = 4       #テトロミノ表示位置（横）
moveY = 0       #テトロミノ表示位置（縦）
type = random.randint(0, 6)        #テトロミノのタイプ

timer = 800     #ゲームスピードコントロール
score = 0       #スコア

color = ["magenta", "blue", "cyan", "yellow", "orange", "red", "green", "black", "white"]

#テトロミノデータ
tetroT = [-1, 0, 0, 0, 1, 0, 0, 1]
tetroJ = [-1, 0, 0, 0, 1, 0, 1, 1]
tetroI = [-1, 0, 0, 0, 1, 0, 2, 0]
tetroO = [ 0, 0, 1, 0, 0, 1, 1, 1]
tetroL = [-1, 0, 0, 0, 1, 0,-1, 1]
tetroZ = [-1,-1, 0,-1, 0, 0, 1, 0]
tetroS = [ 0, 0, 1, 0, 0, 1,-1, 1]
tetro = [tetroT, tetroJ, tetroI, tetroO, tetroL, tetroZ, tetroS]
#フィールドデータ
field = []
for y in range(22):
    sub = []
    for x in range(12):
        if x==0 or x==11 or y==21 :
            sub.append(8)
        else :
            sub.append(7)
    field.append(sub)

#音楽再生
def play_music(file_path):
    global play_obj
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()

#音楽ストップ
def music_stop():
    global play_obj
    if play_obj.is_playing():
        play_obj.stop()
#テトロミノを表示する関数
def drawTetris():
    for i in range(4):
        x = (tetro[type][i*2]+moveX)*SIZE
        y = (tetro[type][i*2+1]+moveY)*SIZE
        can. create_rectangle(x, y, x+SIZE, y+SIZE, fill=color[type])

#フィールドを表示する関数
def drawField():
    for i in range(21):
        for j in range(12):
            outLine=0 if color[field[i+1][j]]=="white" else 1   #白いブロックは枠無しで表示
            can.create_rectangle(j*SIZE, i*SIZE, (j+1)*SIZE, (i+1)*SIZE, fill=color[field[i+1][j]], width=outLine)

#テトロミノを動かす関数
def keyPress(event):   
    global moveX, moveY
    afterX = moveX
    afterY = moveY
    afterTetro = []
    afterTetro.extend(tetro[type])
    if event.keysym=="Right" :      #右移動
        afterX += 1
    elif event.keysym=="Left" :     #左移動
        afterX -= 1
    elif event.keysym=="Down" :     #下移動
        afterY += 1
    elif event.keysym=="space" :    #右回転
        afterTetro.clear()
        for i in range(4):
            afterTetro.append(tetro[type][i*2+1]*(-1))
            afterTetro.append(tetro[type][i*2])
    judge(afterX, afterY, afterTetro)   #アタリ判定関数呼び出し

def judge(afterX, afterY, afterTetro):  #アタリ判定をする関数
    global moveX, moveY
    result = True
    for i in range(4):
        x = afterTetro[i*2]+afterX
        y = afterTetro[i*2+1]+afterY
        if field[y+1][x]!=7 :
            result = False
    if result==True :
        moveX = afterX
        moveY = afterY
        tetro[type].clear()
        tetro[type].extend(afterTetro)
    return result

def dropTetris():
    global moveX, moveY, type, timer
    afterTetro = []
    afterTetro.extend(tetro[type])
    result = judge(moveX, moveY+1, afterTetro)
    if result==False :
        for i in range(4):
            x = tetro[type][i*2]+moveX
            y = tetro[type][i*2+1]+moveY
            field[y+1][x] = type
        deleteLine()
        type = random.randint(0, 6)
        moveX = 4
        moveY = 0
    can.after(timer, dropTetris)
    timer -= 2                          #落下速度コントロール
    if timer<140 :
        timer = 180

def deleteLine():
    global score
    for i in range(1, 21):
        if 7 not in field[i]:
            for j in range(i):
                for k in range(12):
                    field[i-j][k] = field[i-j-1][k]
            score += 800-timer
    for i in range(1, 11):
        if 7 != field[1][i]:

            music_stop()  # 音楽を停止する
            ## スコア送信
            server_url = "http://"+ip_address+":"+port_number+"/receive_data"
            data_to_send = {"得点": score}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(server_url, data=json.dumps(data_to_send), headers=headers)

            messagebox.showinfo("information", "GAME OVER !")
            exit()

####################  ゲームループ  ####################    
def on_button_click():
    print("ボタンがクリックされました")
    root.destroy()


# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Tkinterのボタン例")
# タイトルバーを非表示にする
root.overrideredirect(True)

# ボタンの作成
button = tk.Button(root, text="クリックしてください", command=on_button_click)


# 音楽ファイルのパス
music_file = 'tetris-theme-korobeiniki-arranged-for-piano-186249.wav'

# 音楽再生用のスレッドを作成し、開始する
music_thread = threading.Thread(target=play_music, args=(music_file,))
music_thread.start()

# ボタンの配置
button.pack()
root.mainloop()

win = tk.Tk()
win.geometry("340x630")
win.title("TETRIS")
can = tk.Canvas(win, width=12*SIZE, height=21*SIZE)
can.place(x=-10, y=0)
var = tk.StringVar()
lab = tk.Label(win, textvariable=var, fg="blue", bg="white", font=("", "20"))   #得点表示
lab.place(x=50, y=600)

win.bind("<Any-KeyPress>", keyPress)    #キープレスをバインド

def gameLoop():
    can.delete("all")
    var.set(score)
    drawField()
    drawTetris()
    can.after(50, gameLoop)

gameLoop()
dropTetris()

win.mainloop()
