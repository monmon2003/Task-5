from googletrans import Translator
from datetime import datetime
import pytz

def get_current_time():
    timezone = pytz.timezone('Asia/Kolkata')
    return datetime.now(timezone)


def translate_to_hindi(word):
    vowels = 'AEIOUaeiou'
    if word[0] in vowels:
        print("This word starts with a vowel. Please provide another word.")
    else:
        translator = Translator()
        translated_word = translator.translate(word, src='en', dest='hi').text
        print(f"Translation in Hindi: {translated_word}")
    
def main():
    word = input("Enter an English word: ")
    current_time = get_current_time()
    if current_time.hour != 22:
        print("Please try between 9 PM and 10 PM IST.")
        return
    
    translate_to_hindi(word)
    

if __name__ == "__main__":
    main()