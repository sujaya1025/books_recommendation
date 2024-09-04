from flask import Flask, render_template, request
import pandas as pd
import pickle
import re

app = Flask(__name__)

# Load the preprocessed data and models from pickle files
with open('tfidf_matrix.pkl', 'rb') as file:
    tfidf_matrix = pickle.load(file)

with open('combined_sim.pkl', 'rb') as file:
    combined_sim = pickle.load(file)

with open('books_df.pkl', 'rb') as file:
    books_df = pickle.load(file)

def get_recommendations(title, combined_sim=combined_sim):
    title_lower = title.lower()
    books_df['Title_lower'] = books_df['Title'].str.lower()

    sub = books_df['Title_lower'].str.contains(re.escape(title_lower), case=False, na=False)

    if not sub.any():
        print(f"No books found containing '{title}'.")
        return []
    matching_indices = books_df.index[sub]

    if matching_indices.size > 0:
        idx = matching_indices[0]
    else:
        print(f"No books found containing '{title}'.")
        return []

    # Get the pairwise similarity scores of all books with that book
    sim_scores = list(enumerate(combined_sim[idx]))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar books
    sim_scores = sim_scores[1:11]

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]

    similar_books = books_df[['Title', 'Author', 'Genre', 'Rating', 'Image']].iloc[book_indices]

    return similar_books


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    if request.method == 'POST':
        book_title = request.form['title']
        recommendations = get_recommendations(book_title)
    return render_template('index.html', books=recommendations.to_dict(orient='records') if recommendations is not None else None)

if __name__ == '__main__':
    app.run(debug=True)
