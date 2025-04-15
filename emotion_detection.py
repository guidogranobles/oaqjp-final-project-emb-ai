import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    input_json = {"raw_document": {"text": text_to_analyze}}
    response =  requests.post(URL, headers=Headers, json=input_json).json()
    emotion_result = response["emotionPredictions"][0]["emotion"]

    dominant_emotion_score = 0
    dominant_emotion = ""
    for emotion_name, emotion_score in emotion_result.items():
        if emotion_score > dominant_emotion_score:
            dominant_emotion_score = emotion_score
            dominant_emotion = emotion_name

    emotion_result["dominant_emotion"] = dominant_emotion

    return emotion_result