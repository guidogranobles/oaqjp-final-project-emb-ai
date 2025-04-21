import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    input_json = {"raw_document": {"text": text_to_analyze}}
    response =  requests.post(URL, headers=Headers, json=input_json).json()
    emotions = response["emotionPredictions"][0]["emotion"]

    score = 0
    dominant = ""
    for emotion_name, emotion_score in emotions.items():
        if emotion_score > score:
            score = emotion_score
            dominant = emotion_name

    emotions["dominant_emotion"] = dominant

    return emotions