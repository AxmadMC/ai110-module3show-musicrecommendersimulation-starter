import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

SCORING_MODES = {
    "Genre-First": {"genre": 5, "mood": 3, "energy_close": 2, "energy_similar": 1},
    "Mood-First": {"genre": 3, "mood": 5, "energy_close": 2, "energy_similar": 1},
    "Energy-Focused": {"genre": 2, "mood": 2, "energy_close": 5, "energy_similar": 3},
}
ARTIST_DIVERSITY_PENALTY = 2

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load song rows from a CSV file with numeric fields converted."""
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        songs = []
        for row in csv.DictReader(csv_file):
            for field, converter in numeric_fields.items():
                row[field] = converter(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict, mode: str = "Genre-First") -> Tuple[float, List[str]]:
    """Score a song using the selected recommendation mode."""
    if mode not in SCORING_MODES:
        available_modes = ", ".join(SCORING_MODES)
        raise ValueError(f"Unknown mode {mode!r}. Choose from: {available_modes}")

    weights = SCORING_MODES[mode]
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += weights["genre"]
        reasons.append(f"genre match (+{weights['genre']})")
    if song["mood"] == user_prefs["mood"]:
        score += weights["mood"]
        reasons.append(f"mood match (+{weights['mood']})")

    energy_difference = abs(song["energy"] - user_prefs["energy"])
    if energy_difference <= 0.10:
        score += weights["energy_close"]
        reasons.append(f"close energy (+{weights['energy_close']})")
    elif energy_difference <= 0.25:
        score += weights["energy_similar"]
        reasons.append(f"similar energy (+{weights['energy_similar']})")

    return score, reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    mode: str = "Genre-First",
) -> List[Tuple[Dict, float, str]]:
    """Return top songs while reducing scores for repeated artists."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song, mode)
        scored_songs.append((song, score, reasons))

    recommendations = []
    selected_artists = set()
    while scored_songs and len(recommendations) < k:
        best_index = 0
        best_adjusted_score = float("-inf")
        for index, (song, score, _) in enumerate(scored_songs):
            adjusted_score = score
            if song["artist"] in selected_artists:
                adjusted_score -= ARTIST_DIVERSITY_PENALTY
            if adjusted_score > best_adjusted_score:
                best_index = index
                best_adjusted_score = adjusted_score

        song, score, reasons = scored_songs.pop(best_index)
        if song["artist"] in selected_artists:
            score -= ARTIST_DIVERSITY_PENALTY
            reasons.append(f"repeat artist (-{ARTIST_DIVERSITY_PENALTY})")
        selected_artists.add(song["artist"])

        explanation = ", ".join(reasons) or "No preference matches"
        recommendations.append((song, score, explanation))

    return recommendations
