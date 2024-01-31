import json

def load_scores(file_path):
    try:
        with open(file_path, 'r') as file:
            scores = json.load(file)
        return scores
    except FileNotFoundError:
        return {}

def save_scores(file_path, scores):
    with open(file_path, 'w') as file:
        json.dump(scores, file, indent=4)

def display_ranking(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    print("上位3つのランキング:")
    for i, (name, score) in enumerate(sorted_scores, start=1):
        print(f"{i}.{name},{score}")

def update_score(scores, name, new_score):
    scores[name] = new_score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    scores = dict(sorted_scores[:3])  # 上位3つのスコアのみ保持
    print(f"{name} のスコアが {new_score} に更新されました。")
    file_path = "server/scores.json"
    save_scores(file_path, scores)

def use_ranking(name, score):
    if score is None:
        file_path = "server/scores.json"
        scores = load_scores(file_path)
        print(scores)
        return scores
    else:
        file_path = "server/scores.json"
        scores = load_scores(file_path)
        update_score(scores, name, score)

if __name__ == "__main__":
    name = input("あなたの名前を入力してください: ")
    score = int(input("あなたのスコアを入力してください: "))
    rank = use_ranking(name, score)
    display_ranking(rank)
