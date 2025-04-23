Movie Recommender System
Overview
The Movie Recommender System is a content-based recommendation engine that suggests movies similar to a given input movie. It leverages natural language processing (NLP) techniques and cosine similarity to recommend movies based on their genres, keywords, cast, crew, and plot summaries. The system is built using Python and is designed to provide personalized movie recommendations.
Dataset
The project uses the TMDB 5000 Movie Dataset, which consists of two CSV files:

tmdb_5000_movies.csv: Contains movie metadata such as budget, genres, keywords, overview, popularity, release date, runtime, title, and vote average.
tmdb_5000_credits.csv: Includes cast and crew information for each movie.

The dataset contains approximately 4,800 movies with detailed attributes, which are processed to create a feature-rich representation for recommendation.
Methodology
The recommendation system employs a content-based filtering approach, using the following steps:

Data Preprocessing:

Merge the movies and credits datasets on the movie_id column.
Extract relevant features: movie_id, title, overview, genres, keywords, cast, and crew.
Parse JSON-like columns (genres, keywords, cast, crew) to extract meaningful information (e.g., genre names, top cast, director).
Clean text data by removing spaces (e.g., "Sam Worthington" → "SamWorthington") to ensure consistency in matching.
Split the overview column into individual words.
Combine features into a single tags column, which includes overview words, genres, keywords, cast, and director.


Text Processing:

Convert tags to lowercase for uniformity.
Apply stemming using the Porter Stemmer from NLTK to reduce words to their root form (e.g., "running" → "run").
Use CountVectorizer from scikit-learn to convert the tags column into a numerical feature matrix (bag-of-words model) with a maximum of 5,000 features, excluding English stop words.


Similarity Calculation:

Compute cosine similarity between movie feature vectors to quantify how similar movies are based on their tags.


Recommendation:

For a given movie, retrieve its index in the dataset.
Sort the cosine similarity scores for that movie in descending order.
Return the top 5 most similar movies (excluding the input movie itself).


Serialization:

Save the processed dataset (new_df) and similarity matrix (similarity) as pickle files (movie.pkl and similarity.pkl) for deployment or further use.



Project Structure
movie_recommender_system/
│
├── Dataset/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│
├── movie_recommender_system.ipynb  # Jupyter Notebook with the implementation
├── movie.pkl                      # Pickle file containing processed movie data
├── similarity.pkl                 # Pickle file containing cosine similarity matrix
├── README.md                      # Project documentation

Requirements
The project requires the following Python libraries:

pandas
numpy
nltk
scikit-learn
pickle

Install the dependencies using:
pip install pandas numpy nltk scikit-learn

Additionally, download the NLTK data for the Porter Stemmer:
import nltk
nltk.download('punkt')

Usage

Run the Jupyter Notebook:

Open movie_recommender_system.ipynb in Jupyter Notebook or JupyterLab.
Execute the cells sequentially to preprocess the data, generate the feature vectors, and compute the similarity matrix.


Recommend Movies:

Use the recommend(movie) function by passing the title of a movie (case-insensitive). For example:recommend('batman')


This will print the titles of the top 5 recommended movies.


Deploy or Reuse:

The movie.pkl and similarity.pkl files can be used in a web application or other Python scripts for real-time recommendations.



Example
recommend('avatar')

Output:
ali
titan a.e.
independence day
terminator salvation
battle: los angeles

Limitations

The system relies solely on content-based filtering, which may not capture user preferences or collaborative filtering insights.
The dataset is limited to ~4,800 movies, which may not include recent releases.
The recommendation quality depends on the richness of the tags (e.g., overview, genres, cast, crew). Sparse or incomplete data may lead to suboptimal recommendations.
The CountVectorizer approach may not capture semantic relationships between words (e.g., "war" and "battle"). Advanced techniques like word embeddings (e.g., Word2Vec, BERT) could improve results.

Future Improvements

Incorporate collaborative filtering to account for user ratings and preferences.
Use TF-IDF or word embeddings for better text representation.
Expand the dataset to include more movies or update it with recent releases.
Deploy the system as a web application using frameworks like Flask or Streamlit for user-friendly interaction.
Add filters for recommendations (e.g., by genre, release year, or rating).

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

The TMDB 5000 Movie Dataset is sourced from Kaggle.
Thanks to the open-source community for providing libraries like pandas, scikit-learn, and nltk.

Contact
For questions or suggestions, feel free to open an issue on this repository or contact the project maintainer at [your-email@example.com].
