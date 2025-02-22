import unittest
import json

from EmotionDetection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    def testEmotions(self):

        emotions_test_dict = {"joy": "I am glad this happened",
                              "anger" : "I am really mad about this",
                              "disgust": "I feel disgusted just hearing about this",
                              "sadness": "I am so sad about this",
                              "fear": "I am really afraid that this will happen" }
        for expected_emotion in emotions_test_dict.keys():
            text = emotions_test_dict[expected_emotion]                        
            result = json.loads(emotion_detection.emotion_detector(text))
            self.assertEqual(expected_emotion, result['dominant_emotion'])
            print ("Tested emotion: " + expected_emotion + "; Dominant emotion: " + result['dominant_emotion'] )

unittest.main()
