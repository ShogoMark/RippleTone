#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tracks/<track_id>')
def play_track(track_id):
    # Get the track information from the streaming platform's API or your own database
    track_title = "Track Title"
    track_artist = "Track Artist"
    track_embed_code = "<iframe src='https://streaming-platform.com/embed/track/{track_id}'></iframe>"

    return render_template('play_track.html', track_title=track_title, track_artist=track_artist, track_embed_code=track_embed_code)

if __name__ == '__main__':
    app.run()
