from flask import Flask, request, render_template, jsonify, make_response
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
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] == None:
       return  {"message": "Invalid text! Please try again!."}, 400

    return jsonify(result), 200
