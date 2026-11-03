import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

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

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against genre, mood, and energy preferences."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 5
        reasons.append("genre match (+5)")
    if song["mood"] == user_prefs["mood"]:
        score += 3
        reasons.append("mood match (+3)")

    energy_difference = abs(song["energy"] - user_prefs["energy"])
    if energy_difference <= 0.10:
        score += 2
        reasons.append("close energy (+2)")
    elif energy_difference <= 0.25:
        score += 1
        reasons.append("similar energy (+1)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by preference score."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) or "No preference matches"
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda result: result[1], reverse=True)
    return scored_songs[:k]
