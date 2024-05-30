# CineAdvisor

CineAdvisor is a movie recommendation system that suggests movies based on a given input movie. It uses content-based filtering and leverages movie metadata to compute similarities between movies.

## Features

- Recommends top 5 movies similar to a given movie.
- Displays posters of the recommended movies.
- User-friendly interface built with Streamlit.
- Uses cosine similarity on movie tags derived from genres, keywords, cast, crew, and overview.

## Dataset

The project uses the TMDB 5000 Movie Dataset, which includes information about movies such as genres, keywords, cast, crew, and overview.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Requests
- NLTK
- Scikit-learn
- Pickle

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/CineAdvisor.git
   cd CineAdvisor
   ```

2. Install the required packages:

   ```bash
   pip install streamlit pandas requests nltk scikit-learn
   ```

3. Download the TMDB 5000 Movie Dataset and place it in the project directory.

## Usage

1. Preprocess the dataset to create the required files (`movies.sav` and `similarity.pkl`):

   Run Movie_Recommender_System.ipynb

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open the provided URL in your web browser.

4. Select a movie from the dropdown list and click on "Give me movies" to get recommendations.

## Project Structure

- `app.py`: Main script to run the Streamlit application.
- `tmdb_5000_movies.csv`: Dataset file (should be placed in the project directory).
- `tmdb_5000_credits.csv`: Dataset file (should be placed in the project directory).
- `movies.sav`: Preprocessed movie data.
- `similarity.pkl`: Precomputed similarity matrix.

## How It Works

1. **Data Preprocessing**: The preprocessing script processes the movie dataset to extract relevant features such as genres, keywords, cast, and crew. It then combines these features into a single 'tags' column and vectorizes them.

2. **Vectorization and Similarity Calculation**: The tags are vectorized using `CountVectorizer` and a cosine similarity matrix is computed. This matrix indicates how similar each movie is to every other movie based on their tags.

3. **Recommendation System**: The `recommend` function takes a movie title as input, finds its index, and retrieves the top 5 most similar movies based on the cosine similarity matrix. It also fetches posters for these movies using the TMDB API.

4. **Streamlit App**: The `app.py` script sets up a Streamlit interface where users can select a movie and get recommendations. The app displays the titles and posters of the recommended movies.

## Example

To get recommendations for the movie "Up", you would select "Up" from the dropdown and click "Give me movies". The app will display the titles and posters of the top 5 recommended movies.

## Credits

This project uses data from [The Movie Database (TMDB)](https://www.themoviedb.org/).

