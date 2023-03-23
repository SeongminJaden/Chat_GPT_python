import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import openai
import os

openai.api_key = ""

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('듣고있어요')
        audio = r.listen(source)


    try:
       text = r.recognize_google(audio, language='ko')
       print(text)

    except sr.UnknownValueError:
        print('인식실패')
        continue
    except sr.RequestError as e:
        print('요청실패: {0}'.format(e))

    response = openai.Completion.create(
           model="text-davinci-003",
           prompt=text,
           temperature=0.9,
           max_tokens=2048,
           top_p=1,
           frequency_penalty=0,
           presence_penalty=0.6
    )

    generated_text = response.choices[0].text
    print(generated_text)
    file_path = "sample.mp3"
    os.remove(file_path)
    file_name = 'sample.mp3'
    tts_ko = gTTS(text=generated_text, lang='ko')
    tts_ko.save(file_name)
    playsound(file_name)