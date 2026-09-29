import json
import os

SCORES_FILE = "scores.json"


def load_scores():
    """Return the list of saved scores, or an empty list if none exist yet."""
    if not os.path.exists(SCORES_FILE):
        return []

    with open(SCORES_FILE, "r") as f:
        return json.load(f)


def save_score(player_name, points):
    """Add a new score and save the updated list back to the file."""
    scores = load_scores()
    scores.append({"name": player_name, "points": points})

    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def get_top_scores(limit=5):
    """Return the top scores, highest first."""
    scores = load_scores()
    sorted_scores = sorted(scores, key=lambda s: s["points"], reverse=True)
    return sorted_scores[:limit]
if __name__ == "__main__":
    save_score("Test Player", 50)
    save_score("Another Player", 80)
    print("Top scores:", get_top_scores())