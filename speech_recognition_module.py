import speech_recognition as sr


def input_voice_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ru-RU")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Try again")
        return 1
    except sr.RequestError as e:
        print("Service error; {0}".format(e))
        return 1


if __name__ == '__main__':
    command = input_voice_command()
