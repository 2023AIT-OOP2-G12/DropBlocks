import json

def load_scores(file_path):
    try:
        with open(file_path, 'r') as file:
            scores = json.load(file)
        return scores
    except FileNotFoundError:
        return []

def save_scores(file_path, scores):
    with open(file_path, 'w') as file:
        json.dump(scores, file, indent=4)

def display_ranking(scores):
    sorted_scores = sorted(scores, reverse=True)[:3]
    print("上位3つのランキング:")
    for i, score in enumerate(sorted_scores, start=1):
        print(f"{i}. スコア: {score}")

def update_score(scores, new_score):
    scores.append(new_score)
    scores.sort(reverse=True)
    scores = scores[:3]  # 上位3つのスコアのみ保持
    print(f"スコアが更新されました。")
    file_path = "scores.json"
    save_scores(file_path, scores)

def use_ranking(score):
    file_path = "scores.json"
    scores = load_scores(file_path)
    update_score(scores,score)
    return scores[:3] # 上位3つのスコアのみ送る

if __name__ == "__main__":
    rank=use_ranking(900)
    for i, score in enumerate(rank[:3], start=1):
        print(f"{i}. スコア: {score}")

