from flask import Flask, jsonify, render_template
from flask import request
from flask import Response
from flask import redirect

from EmotionDetection import emotion_detection


app = Flask("Emotions detector")


@app.route("/")
def displayInputPage():
    return app.render_template("index.html")


if __name__ == "__main__":
    app.run()