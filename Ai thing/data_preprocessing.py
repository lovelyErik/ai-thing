import mltk 
from mltk.stem import PorterStemmer
import json
import pickle
import numpy as np


stemmer=PorterStemmer()
words=[]
classes=[]
word_tags_list=[]
ignore_words=["?","!","'s","'m",",","."]


train_data_file=open("intents.json").read()
intents=json.loads(train_data_file)


def get_stem_words(words,ignore_words):
    stem_words=[]
    for word in words:
        if word not in ignore_words:
            w=stemmer.stem (word.lower)
            stem_words.append(w)
    return (stem_words)




    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

for intent in intents["intents"]:
   for pattern in intents["patterns"]:
       pattern_words=mltk.word_tokenize(pattern)
       words.extend(pattern_words),
       word_tags_list.append(pattern_words, intents ["tag"])
   if intents["tag"] not in classes:
       classes.append(intents["tag"])
       stem_words=get_stem_words(words,ignore_words)
print (stem_words)
print (word_tags_list[0])
print (classes)