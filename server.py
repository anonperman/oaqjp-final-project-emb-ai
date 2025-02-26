""" module runnung flask server for sentiment analysis """

import json
from flask import Flask, render_template
from flask import request
from EmotionDetection import emotion_detection

app = Flask("Emotions detector")

@app.route("/")
def display_input_iage():
    """show index html."""
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion():
    """get emotion analysis from nlp server"""
    emotion_str = emotion_detection.emotion_detector(request.args.get('textToAnalyze'))
    result = json.loads(emotion_str)

    if not result['dominant_emotion']:
        return "Invalid text! Please try again!"

    result_str = "For the given statement, the system response is "
    result_str += "\"" + "anger" + "\": " + str(result["anger"])
    result_str += ", \"" + "disgust" + "\": " + str(result["disgust"])
    result_str += ", \"" + "fear" + "\": " + str(result["fear"]) + ", "
    result_str += ", \"" + "joy" + "\": " + str(result["joy"]) + " and "
    result_str += "\"" + "sadness" + "\": " + str(result["sadness"]) + ". "
    result_str += "The dominant emotion is " + result['dominant_emotion'] + "."

    return result_str

if __name__ == "__main__":
    app.run()
