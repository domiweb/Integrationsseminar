import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from nltk.corpus import stopwords
import pickle
import numpy as np
import random
import json

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


lemmatizer = WordNetLemmatizer()

with open('dataset 2.json', 'r+') as f:
    data = json.load(f)

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
botmedix = load_model('botmedix.h5')


stop_words = stopwords.words('english')
stop_words.extend(['The', 'patient', 'suffering'])
def clean_up_sentence(sentence, stop_words=stop_words):
  sentence_words = nltk.word_tokenize(sentence)
  sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words if word not in stop_words]
  return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = botmedix.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x : x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    list_of_intents = intents_json['intents']
    if len(intents_list) > 1:
        tag = [i['intent'] for i in intents_list]
        prob = [i['probability'] for i in intents_list]
        result = []
    # list_of_intents
        for i, k in enumerate(tag):
            for j in list_of_intents:
                if j['tag'] == k:
                    tmp = float(prob[i]) * 100
                    result.append(random.choice(j['responses']) + ' with the probability of ' + str(round(tmp, 2)) + '%')
                    break
    else:
        tag = intents_list[0]['intent']
        prob = intents_list[0]['probability']
        for i in list_of_intents:
            if i['tag'] == tag:
                response_ = random.choice(i['responses'])
                if response_.startswith('Are there further symptoms like'):
                    result = response_
                else:
                    tmp = float(prob) * 100
                    result = response_ + ' with the probability of ' + str(round(tmp, 2)) + '%'
                break
    return result

print("Go! Botmedix is working")

