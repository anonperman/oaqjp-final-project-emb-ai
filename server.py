from flask import Flask, jsonify, render_template
from flask import request
from flask import Response
from flask import redirect

from EmotionDetection import emotion_detection


app = Flask("Emotions detector")


@app.route("/")
def displayInputPage():
    return render_template("index.html")

@app.route("/emotionDetector")
def getEmotion():
    result = json.loads(emotion_detection.emotion_detector(request.args.get('textToAnalyze')))
    result_str = "For the given statement, the system response is "
    for emotion in emotions_test_dict.keys():
        result_str += "\" + emotion + "\\\": " + float(result[expected_emotion]) + ","
        self.assertEqual(expected_emotion, result['dominant_emotion'])    


if __name__ == "__main__":
    app.run()