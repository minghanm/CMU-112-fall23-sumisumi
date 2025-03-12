import json

class Leaderboard:
    def __init__(self, filename):
        self.filename = filename
        self.scores = self.load_scores() or []

    def load_scores(self):
        try:
            with open(self.filename, 'r') as file:
                scores = json.load(file)
        except FileNotFoundError:
            scores = []
        return scores

    def save_scores(self):
        with open(self.filename, 'w') as file:
            json.dump(self.scores, file, indent=4)

    def add_score(self, player_name, score):
        self.scores.append({"player_name": player_name, "score": score})
        self.scores.sort(key=lambda x: x["score"], reverse=True)  # Sort scores in descending order
        self.save_scores()

    def get_leaderboard(self, num_entries=10):
        return self.scores[:num_entries]