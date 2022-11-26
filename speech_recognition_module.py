import speech_recognition as sr


def input_voice_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="ru-RU")
        print(command)
        return command
    except sr.UnknownValueError:
        print("Робот не расслышал фразу")
        return 1
    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))
        return 1


if __name__ == '__main__':
    while True:
        input_voice_command()
