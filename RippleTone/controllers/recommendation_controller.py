from flask import render_template
import requests

# Music recommendation action based on artist
def recommend_by_artist(artist_name):
    # Fetch recommendation data from the external API based on the artist
    recommendations = fetch_recommendations_by_artist(artist_name)

    # Render the recommendation template with the data
    return render_template('recommendation/recommend.html', recommendations=recommendations)

# Music recommendation action based on genre
def recommend_by_genre(genre_name):
    # Fetch recommendation data from the external API based on the genre
    recommendations = fetch_recommendations_by_genre(genre_name)

    # Render the recommendation template with the data
    return render_template('recommendation/recommend.html', recommendations=recommendations)

# Fetch recommendation data from the external API based on the artist
def fetch_recommendations_by_artist(artist_name):
    # Make a request to the external API, passing the artist name as a parameter
    response = requests.get(f'https://api.example.com/recommendations?artist={artist_name}')

    # Extract recommendation data from the API response
    if response.status_code == 200:
        recommendations = response.json()
    else:
        recommendations = []

    return recommendations

# Fetch recommendation data from the external API based on the genre
def fetch_recommendations_by_genre(genre_name):
    # Make a request to the external API, passing the genre name as a parameter
    response = requests.get(f'https://api.example.com/recommendations?genre={genre_name}')

    # Extract recommendation data from the API response
    if response.status_code == 200:
        recommendations = response.json()
    else:
        recommendations = []

    return recommendations