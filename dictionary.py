from keytotext import pipeline
from PyDictionary import PyDictionary
import pyttsx3
import threading
import keyboard
"""
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


nlp = pipeline("k2t")
config = {"do_sample": True, "num_beams": 4, "no_repeat_ngram_size": 3, "early_stopping": True}
#print(nlp(['Me','happy'], **config))
"""
global engine
engine = None 

def play_voice():    
    engine = pyttsx3.init()
    engine.say(search)
    engine.runAndWait()
    engine = None
    
        

def listen_for_s():
    keyboard.wait('s')
    play_voice()


global search 

key1 = "Noun"
key2 = 'Verb'
key3 = 'Adjective'
key4 = 'Adverb'

dictionary=PyDictionary()#for translate

nlp = pipeline("k2t")#for creating sentence
config = {"do_sample": True, "num_beams": 4, "no_repeat_ngram_size": 3, "early_stopping": True}



listener_thread = threading.Thread(target=listen_for_s)
listener_thread.start()



while True:
    
    search = input("\nEnter the word you want to search or enter -1 to exit\n")
    if(search == "-1"):
        break
    else:
        result = dictionary.meaning(search)
        #print(result)
        if(result):            
            try:                    
                if(key1 in result):
                    print("\nNoun:",result[key1][0])
                elif key2 in result:
                    print("\nVerb:",result[key2][0])
                elif key3 in result:
                    print("\nAdjective:",result[key3][0])
                elif key4 in result:
                    print("\nAdverb:",result[key4][0])
                else:
                    pass
                print("\nExample:")
                print(nlp([search], **config))
                print("\nYou can press 's' to hear the pronunciation ")
            except:
                pass
        else:
            print("\nThis means that you enter a wrong vocabulary,please input again\nOr the dictionart don't support this word,Sorry")