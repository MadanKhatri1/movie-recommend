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
```

Additionally, download the NLTK data for the Porter Stemmer:
```bash
import nltk
nltk.download('punkt')
```
## Usuage

# Run the Jupyter Notebook:
   - Open movie_recommender_system.ipynb in Jupyter Notebook or JupyterLab.
   - Execute the cells sequentially to preprocess the data, generate the feature vectors, and compute the similarity matrix.
   - Use the recommend(movie) function by passing the title of a movie (case-insensitive). For example:
     `bash recommend('batman')`
   -The movie.pkl and similarity.pkl files can be used in a web application or other Python scripts for real-time recommendations.


## Limitations
- The system relies solely on content-based filtering, which may not capture user preferences or collaborative filtering insights.
- The dataset is limited to ~4,800 movies, which may not include recent releases.
- The recommendation quality depends on the richness of the tags (e.g., overview, genres, cast, crew). Sparse or incomplete data may lead to suboptimal recommendations.
- The CountVectorizer approach may not capture semantic relationships between words (e.g., "war" and "battle"). Advanced techniques like word embeddings (e.g., Word2Vec, BERT) could improve results.
