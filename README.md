# Movie Recommender System

## Overview
The **Movie Recommender System** is a content-based recommendation engine that suggests movies similar to a given input movie. It leverages natural language processing (NLP) techniques and cosine similarity to recommend movies based on their genres, keywords, cast, crew, and plot summaries. The system is built using Python and is designed to provide personalized movie recommendations.

## Dataset
The project uses the **TMDB 5000 Movie Dataset**, which consists of two CSV files:
- **tmdb_5000_movies.csv**: Contains movie metadata such as budget, genres, keywords, overview, popularity, release date, runtime, title, and vote average.
- **tmdb_5000_credits.csv**: Includes cast and crew information for each movie.

The dataset contains approximately 4,800 movies with detailed attributes, which are processed to create a feature-rich representation for recommendation.

## Methodology
The recommendation system employs a content-based filtering approach, using the following steps:

1. **Data Preprocessing**:
   - Merge the movies and credits datasets on the `movie_id` column.
   - Extract relevant features: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.
   - Parse JSON-like columns (`genres`, `keywords`, `cast`, `crew`) to extract meaningful information (e.g., genre names, top cast, director).
   - Clean text data by removing spaces (e.g., "Sam Worthington" → "SamWorthington") to ensure consistency in matching.
   - Split the `overview` column into individual words.
   - Combine features into a single `tags` column, which includes overview words, genres, keywords, cast, and director.

2. **Text Processing**:
   - Convert `tags` to lowercase for uniformity.
   - Apply stemming using the **Porter Stemmer** from NLTK to reduce words to their root form (e.g., "running" → "run").
   - Use **CountVectorizer** from scikit-learn to convert the `tags` column into a numerical feature matrix (bag-of-words model) with a maximum of 5,000 features, excluding English stop words.

3. **Similarity Calculation**:
   - Compute **cosine similarity** between movie feature vectors to quantify how similar movies are based on their tags.

4. **Recommendation**:
   - For a given movie, retrieve its index in the dataset.
   - Sort the cosine similarity scores for that movie in descending order.
   - Return the top 5 most similar movies (excluding the input movie itself).

5. **Serialization**:
   - Save the processed dataset (`new_df`) and similarity matrix (`similarity`) as pickle files (`movie.pkl` and `similarity.pkl`) for deployment or further use.


## Requirements
The project requires the following Python libraries:
- `pandas`
- `numpy`
- `nltk`
- `scikit-learn`
- `pickle`

Install the dependencies using:
```bash
pip install pandas numpy nltk scikit-learn


