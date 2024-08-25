"""This module uses Watson AI Bert Sentiment from IBM to set the score of a given text."""
# Import the requests library to handle HTTP requests
import json
import requests
def sentiment_analyzer(text_to_analyse):
    ''' Function named sentiment_analyzer that takes a string input (text_to_analyse) 
    '''
    # URL of the sentiment analysis service
    url1 = 'https://sn-watson-sentiment-bert.labs.skills.network/'
    url2 = 'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    url = url1 + url2

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=15)
    label = ""
    score = ""
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    # Return the response text from the API
    res = {'label':label, 'score':score}
    return res
