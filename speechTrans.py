import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os
#create Recognizer() class 2 objects
reco1 = spr.Recognizer() 
reco2 = spr.Recognizer() 

#create microphone instance with device microphone chosen whose index value is 0
mc = spr.Microphone(device_index=0)
#capture voice
with mc as source:
    print("Speak 'Hello' to start the Translation!")
    print("---------------------------------------")
    audio = reco1.listen(source)

#Based on speech, translate the sentence into another language
if 'hello' in reco1.recognize_google(audio):
    reco1 = spr.Recognizer()
    translator = Translator()
    from_lang = 'en'
    to_lang ='hi'
    with mc as source:
        print('Speak a Sentence...')
        audio = reco2.listen(source)
        #get_sentence = reco2.recognize_google(audio)

        try:
            get_sentence = reco2.recognize_google(audio)
            print("Phrase to be Translated: " + get_sentence)
            text_to_translate = translator.translate(get_sentence, src = from_lang, dest = to_lang)
            text = text_to_translate.text
            speak = gTTS(text = text, lang = to_lang ,slow= False)
            speak.save("translated_voice.mp3")
            os.system("start translated_voice.mp3")
        
        except spr.UnknownValueError:
            print("Unable to understand the input..")
        except spr.RequestError as e:
            print("Unable to provide required output".format(e))    
