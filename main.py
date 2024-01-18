from flask import Flask, request, render_template
from ranking import use_ranking
from ranking import update_score
app = Flask(__name__)

@app.route('/')
def index():
    ranking_data=use_ranking(0)
    print(ranking_data)

    return render_template('index.html',ranking_data=ranking_data)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json  # POSTで送信されたJSONデータを受け取る例
    update_score(data)
    print("Received data:", data)
    return "Data received successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # ポート番号を5001に変更

