# books_recommender
This is a book recommendation system built with Flask. It suggests books based on a given title using a similarity-based approach.

Features:
- Book Recommendations: Suggests books similar to the input title based on similarity scores.
- User Interface: Simple web form for inputting book titles and viewing recommendations.

Files
- data_scrape.ipynb:
This notebook contains code for scraping book data from goodreads.com.
- books_rec.ipynb:
This notebook includes code for processing text data using TF-IDF.
- books_final: CSV file with scraped data
- app.py: Main Flask application.
- templates folder: Contains HTML (index.html) template for the web pages.
- tfidf_matrix.pkl, combined_sim.pkl, books_df.pkl: Preprocessed data files.
