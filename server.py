from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSON_SORT_KEYS"]              = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_analyzer():
    textToAnalyze = request.args["textToAnalyze"]
    result = emotion_detector(textToAnalyze)
    return jsonify(result)
