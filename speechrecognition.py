import speech_recognition as sr

speechrecog = sr.Recognizer

with sr.Microphone() as source:
    print('Speak What You want to speak')
    audio = speechrecog.listen(source)

    try:
        text = speechrecog.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("I did not recognize what you said")

