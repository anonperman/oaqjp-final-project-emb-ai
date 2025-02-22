import sys
import requests
import json


## function to run emotion detection using the appropriate Emotion
## Detection function.
## Note: Assume that that text to be analyzed is passed to the function 
## as an argument and is stored in the variable text_to_analyze. 
## The value being returned must be the text attribute of the response 
## object as received from the Emotion Detection function.
##
def emotion_detector(text_to_analyze):

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=Headers)
    # print (json.dumps(response.text, indent=4))

    if response.status_code == 400:
        return json.dumps({
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
        })

    resp_dict = json.loads(response.text)
    emotions_list = resp_dict["emotionPredictions"][0]["emotionMentions"][0]["emotion"]

    max_emotion = ""
    max_val = 0
    for emotion in emotions_list:
        name = emotion
        value = emotions_list[emotion]
        if value > max_val:
            max_val = value
            max_emotion = emotion

    new_emotions_json = emotions_list
    emotions_list['dominant_emotion'] = max_emotion
    return json.dumps(emotions_list, indent=4)

if __name__ == '__main__':
    fResponse = emotion_detector(sys.argv[1])
    print(fResponse)