import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser
#setting up voice
bot=pyttsx3.init('sapi5')
voices=bot.getProperty('voices')
bot.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN_US_ZIRA_11.0')
#text to audio
def speak(audio):
    bot.say(audio)
    bot.runAndWait()
speak('Hi there, I am Nora')

def speech():
    variable=sr.Recognizer()
    #loop
    #microphone used
    with sr.Microphone() as source:
        #wait
        print("Speak friend.....")
        #waiting to capture speech
        variable.pause_threshold=0.6
        #variable with listen function captures voice stored in source through microphone and stores in in a variable audio
        audio=variable.listen(source)

    try:
        #ask determines what u said by google speech API
        ask=variable.recognize_google(audio, language='en-us')
        print(f"you said:{ask}")
    except Exception:#if u said nothing
        print("Say that again")
        return ""

    return ask
if __name__ == '__main__':
    while True:
        query=speech().lower()
        print(query)

        try:#if wolframalpha doesnt have your answer
           if 'Nora' in query:
              query=query.replace('Nora','')#to remove nora whle sending to wolframalpha
              client=wolframalpha.Client("L77A8L-97HJHAGAKQ")#your api key
              result=client.query(query)
              answer=next(result.results).text
              print(answer)
              speak(answer)
        except Exception:
            try:#if wikipedia also doesnt have the answer
                query=query.replace('Nora','')
                results=wikipedia.summary(query,sentence=2)
                print(results)
                speak(results)
            except Exception:
                try:
                   query = query.replace('Nora', '')
                   webbrowser.open('https://google.com/?#q='+query)
                except Exception:
                    print('I am sorry, but I didnt fing your required result;Plz re run the program')
                    speak('I am sorry, but I didnt fing your required result;Plz re run the program')