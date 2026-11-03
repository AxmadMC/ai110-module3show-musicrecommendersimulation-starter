# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---This recommender is designed to generate personalized music recommendations based on a user's preferred genre, mood, and energy level. It assumes that users can describe their musical preferences using these features. The project is intended for classroom exploration of recommendation systems and demonstrates how content-based filtering can be used to recommend songs.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---The recommender compares song characteristics with a user's preferences. It uses features such as genre, mood, and energy from each song and compares them to the user's preferred values. Songs earn points when their genre and mood match the user's preferences, and additional points are awarded when the song's energy level is close to the user's preferred energy level. The total score determines how relevant a song is to the user, and songs are ranked from highest to lowest score before being recommended. Compared with the starter logic, the recommendation process was analyzed and documented to better explain how features and ranking influence results.

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---The dataset contains approximately 30 songs representing a variety of genres and moods, including pop, rock, lofi, jazz, ambient, indie pop, and synthwave. Moods include happy, chill, focused, intense, relaxed, and moody. No songs were removed from the original dataset. While the dataset captures several common music characteristics, it does not include many factors that influence musical taste, such as listening history, artist popularity, cultural preferences, lyrics, or social trends.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---The system works well for users whose preferences closely match genres and moods represented in the dataset. It successfully identifies songs that share important characteristics with a user's preferences and generally produces recommendations that match expected musical vibes. The scoring system captures the relationship between genre, mood, and energy effectively, and the recommendations often align with intuitive expectations.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

## Algorithmic Approach
This recommender uses content-based filtering. Songs are compared against user preferences for genre, mood, and energy. Points are awarded for matching genres and moods, while additional similarity points are given for energy levels that closely match user preferences. Songs are ranked by total score and returned as recommendations with explanations.

This recommender strongly favors genre matches, which can create a filter bubble where users repeatedly receive songs from the same genre. Because the dataset contains only about 30 songs, recommendations may lack diversity. The model only uses genre, mood, and energy when making recommendations. As a result, some songs that users might enjoy could be ranked lower because other features such as danceability, valence, and acousticness are ignored.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---Profiles Tested

1. Happy Pop
2. Chill Lofi
3. Intense Rock
4. Bluegrass Euphoric (edge case)
5. Metal Chill (edge case)
6. K-pop Calm (edge case)

Results

The Happy Pop profile recommended songs such as Sunrise City because they matched the preferred genre, mood, and energy level.

The Chill Lofi profile recommended calmer songs with lower energy values.

The Intense Rock profile favored high-energy songs with more intense moods.

The edge-case profiles revealed weaknesses in the system. Profiles with genres that did not exist in the dataset received weaker recommendations because there were no genre matches available.

Observations

Genre had the strongest influence on recommendations because it received the highest score weight. When user preferences changed, recommendation rankings changed as expected.

Comparison

The Pop profile preferred upbeat and energetic songs, while the Lofi profile preferred calmer and more relaxing songs. The Rock profile favored intense and high-energy tracks. This shows that the recommender responds appropriately to different user preferences.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---Future improvements could include incorporating additional song features such as danceability, valence, acousticness, artist popularity, and release year. Recommendation explanations could be made more detailed to help users understand why songs were selected. Diversity techniques could also be added to prevent too many recommendations from the same genre or artist. Finally, the system could support more complex user tastes by learning from listening history rather than relying only on manually entered preferences.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
- This project helped me understand how recommendation systems convert user preferences and song features into rankings. One interesting discovery was how strongly feature weights influence recommendations and how small changes to the scoring formula can significantly affect results. The project also showed how recommendation systems can develop bias or create filter bubbles when they rely too heavily on a small set of features. As a result, I now better understand how music streaming platforms personalize recommendations for users.

## Experiment

I tested removing the mood feature from the scoring system. Recommendations became more dependent on genre and energy level. This showed that mood contributes significantly to recommendation quality and helps distinguish songs that would otherwise receive similar scores.