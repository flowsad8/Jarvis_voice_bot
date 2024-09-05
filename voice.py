import speech_recognition as sr
import webbrowser
import pyglet





while True:
    r = sr.Recognizer()

    try:

        with sr.Microphone(device_index = 1) as source:
            print("Слушаю")        
            audio = r.listen(source)


        query = r.recognize_google(audio, language = 'ru-RU')


        inpit = ("Вы сказали " + query.lower())
        print(inpit)
        a = query.lower()

        jarvis = ['fd','джарвис', 'ренат', 'jarvis', 'ринат']
        off = ['отключись', 'выключись', 'вырубись','выключи']
        ass = 0
        tries = 0



        asss = 0
        while asss == 0:
            if off[tries] in a:
                print ("отключаюсь")
                a = f + d
            else:
                tries = tries + 1    
                if tries == 2:
                    asss = 1

        if "открой яндекс" in a:
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://www.yandex.ru/")
        if "открой whatsapp" in a:
                    
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://web.whatsapp.com/")
        if "открой телегу" in a:
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://web.telegram.org/")
        if "открой telegram" in a:
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://web.telegram.org/")    
        if "открой вк" in a:
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://vk.com/")
        if "открой youtube" in a:
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://www.youtube.com/")
        if "открой discord" in a:
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://discord.com/") 
        if "включи музыку" in a:
            song = pyglet.media.load('prompt_loading.mp3')
            song.play()
            print ("Загружается...")
            webbrowser.open("https://www.youtube.com/watch?v=ArJlhqDKt-M")


        while ass == 0:
            if jarvis[tries] in a:
                print ("да, сэр")



                print ("да, сэр")
                ass = 1
                tries = 0
            else:
                tries = tries + 1
                if tries == 4:
                    ass = 1
                    tries = 0
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")

    except sr.RequestError as e:

        print("[log] Неизвестная ошибка, проверьте интернет!")