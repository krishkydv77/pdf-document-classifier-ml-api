
import re     #special characters remove karne ke liya
import nltk  #Natural Language Toolkit =>Text processing karti ha

from nltk.corpus import stopwords    #Common useless words remove karne ke liye.
from nltk.tokenize import word_tokenize   #Sentence ko words me todta hai.

nltk.download("punkt")  #Ye text ko words/sentences me todne ke liye use hota hai.
nltk.download("punkt_tab")
nltk.download("stopwords")  #Tokenizer aur stopword dataset download karta hai.

STOP_WORDS = set(stopwords.words("english"))  #English stopwords ko set me store karta hai. ex.is /the ,are => set()

def preprocess_text(text):    #

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)   #Special symbols remove karta hai. =>regex 

    tokens = word_tokenize(text)

    filtered_tokens = [                     #Useless words remove karta hai.
        word for word in tokens
        if word not in STOP_WORDS
    ]

    return " ".join(filtered_tokens)  #Words ko dubara sentence me convert karta hai.
