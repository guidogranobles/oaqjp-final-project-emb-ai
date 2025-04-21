from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSON_SORT_KEYS"] = False

@app.route("/")
def index():
    """Return lading page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Return result of emotion analysis."""
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return {"message": "Invalid text! Please try again!."}, 400

    return jsonify(result), 200
