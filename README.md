# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

## How The System Works
-Real-world recommendation systems such as Spotify and YouTube use information about users and songs to predict what listeners might enjoy next. Many platforms combine collaborative filtering, which learns from the behavior of similar users, with content-based filtering, which compares song attributes. This project focuses on content-based filtering by comparing a user's preferred genre, mood, energy, valence, danceability, and acousticness with the features of songs in the dataset. Each song receives a weighted score based on how closely it matches the user's preferences, and the songs are ranked from highest to lowest score to generate recommendations.
## Song Features
- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness
- UserProfile Features
- preferred_genre
- preferred_mood
- preferred_energy
- preferred_valence
- preferred_danceability
- preferred_acousticness

### Algorithm Recipe
The recommender compares each song's genre, mood, energy, valence, danceability, and acousticness with the user's preferences. Songs receive points for genre and mood matches, plus similarity points for numerical features. The system calculates a total score for each song, sorts songs from highest to lowest score, and recommends the top matches.

## Expected Biases
This recommender may favor songs from matching genres and overlook songs that have a similar vibe but belong to different genres. Because the dataset is small, recommendations may also become repetitive.

## Sample Recommendation Output
Top recommendations:

- Sunrise City - Score: 10.00
Because: genre match (+5), mood match (+3), close energy (+2)

- Gym Hero - Score: 6.00
Because: genre match (+5), similar energy (+1)

- Rooftop Lights - Score: 5.00
Because: mood match (+3), close energy (+2)

- Night Drive Loop - Score: 2.00
Because: close energy (+2)

- Neon Orchard - Score: 2.00
Because: close energy (+2)

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



## Evaluation Notes

The Happy Pop profile produced the most accurate recommendations because songs matched genre, mood, and energy preferences. Edge-case profiles such as K-pop Calm revealed limitations because the dataset did not contain matching genres. This demonstrated that the recommender relies heavily on genre matching and may create a filter bubble by repeatedly recommending similar songs.