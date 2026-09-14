"""
Flask server for the Emotion Detection application.
Provides an endpoint to analyze emotional content in text.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Endpoint that receives text input, processes it through the
    emotion detector, and returns a formatted response string.
    Handles invalid or blank input by returning an error message.
    """
    text_to_analyze = request.args.get("text")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
