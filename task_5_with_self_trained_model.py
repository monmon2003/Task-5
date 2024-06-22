from googletrans import Translator
from datetime import datetime
import pytz
import json
from keras.models import load_model
from keras.preprocessing.text import tokenizer_from_json
from keras.utils import pad_sequences
import numpy as np


model_2 = load_model('english_to_hindi_model')


with open('english_tokenizer.json') as f:
    data = json.load(f)
    english_tokenizer = tokenizer_from_json(data)
    


with open('hindi_tokenizer.json') as f:
    data = json.load(f)
    hindi_tokenizer = tokenizer_from_json(data)
    


with open('sequence_length_hindi.json') as f:
    max_length_hn = json.load(f)
    
def pad(x, length=None):
    return pad_sequences(x, maxlen=length, padding='post')

def translate(english_sentence):
    english_sentence = english_sentence.lower()
    
    english_sentence = english_sentence.replace(".", '')
    english_sentence = english_sentence.replace("?", '')
    english_sentence = english_sentence.replace("!", '')
    english_sentence = english_sentence.replace(",", '')
    
    english_sentence = english_tokenizer.texts_to_sequences([english_sentence])
    english_sentence = pad(english_sentence, max_length_hn)
    
    english_sentence = english_sentence.reshape((-1,max_length_hn))
    
    hindi_sentence = model_2.predict(english_sentence)[0]
    
    hindi_sentence = [np.argmax(word) for word in hindi_sentence]

    hindi_sentence = hindi_tokenizer.sequences_to_texts([hindi_sentence])[0]
    
    print("hindi translation: ", hindi_sentence)
    
    return hindi_sentence

def get_current_time():
    timezone = pytz.timezone('Asia/Kolkata')
    return datetime.now(timezone)


def translate_to_hindi(word):
    vowels = 'AEIOUaeiou'
    if word[0] in vowels:
        print("This word starts with a vowel. Please provide another word.")
    else:
        
        translated_word = translate(word)
        print(f"Translation in Hindi: {translated_word}")
    
def main():
    word = input("Enter an English word: ")
    current_time = get_current_time()
    if current_time.hour != 21:
        print("Please try between 9 PM and 10 PM IST.")
        return
    
    translate_to_hindi(word)
    

if __name__ == "__main__":
    main()