"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    modes = {
        "1": "Genre-First",
        "2": "Mood-First",
        "3": "Energy-Focused",
    }
    print("Choose a recommendation mode:")
    for choice, mode_name in modes.items():
        print(f"{choice}. {mode_name}")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in modes:
            mode = modes[choice]
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    print(f"\nActive recommendation mode: {mode}")
    recommendations = recommend_songs(user_prefs, songs, k=5, mode=mode)

    headers = ("Song Title", "Score", "Reasons")
    rows = [
        (song["title"], f"{score:.2f}", explanation)
        for song, score, explanation in recommendations
    ]
    widths = [
        max([len(header)] + [len(row[index]) for row in rows])
        for index, header in enumerate(headers)
    ]
    border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    print("\nTop recommendations:")
    print(border)
    print("| " + " | ".join(header.ljust(width) for header, width in zip(headers, widths)) + " |")
    print(border)
    for row in rows:
        print("| " + " | ".join(value.ljust(width) for value, width in zip(row, widths)) + " |")
    print(border)


if __name__ == "__main__":
    main()

    pop_profile = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.80
}

lofi_profile = {
    "genre": "lofi",
    "mood": "chill",
    "energy": 0.40
}

rock_profile = {
    "genre": "rock",
    "mood": "intense",
    "energy": 0.90
}
