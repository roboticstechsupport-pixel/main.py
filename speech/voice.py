"""
==========================================================
Project ULTRON
Voice Engine
==========================================================
"""

import threading
import speech_recognition as sr
import pyttsx3


class VoiceEngine:

    def __init__(self, config):

        self.config = config

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.engine = pyttsx3.init()

        self.engine.setProperty(
            "rate",
            config.SPEECH_RATE
        )

        self.engine.setProperty(
            "volume",
            config.SPEECH_VOLUME
        )

        self.running = False

        self.speaking = False

        print("[Voice] Engine Created")

    #######################################################

    def initialize(self):

        print("[Voice] Initializing...")

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

        self.running = True

        print("[Voice] Ready")

    #######################################################

    def speak(self, text):

        if not text:
            return

        self.speaking = True

        print(f"ULTRON : {text}")

        self.engine.say(text)

        self.engine.runAndWait()

        self.speaking = False

    #######################################################

    def speak_async(self, text):

        threading.Thread(
            target=self.speak,
            args=(text,),
            daemon=True
        ).start()

    #######################################################

    def listen(self, timeout=5):

        try:

            with self.microphone as source:

                print("[Listening...]")

                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=10
                )

            text = self.recognizer.recognize_google(audio)

            print("You :", text)

            return text

        except sr.WaitTimeoutError:

            return ""

        except sr.UnknownValueError:

            return ""

        except sr.RequestError:

            return ""

        except Exception as e:

            print(e)

            return ""

    #######################################################

    def listen_forever(self, callback):

        while self.running:

            text = self.listen()

            if text:

                callback(text)

    #######################################################

    def start_background_listener(self, callback):

        thread = threading.Thread(
            target=self.listen_forever,
            args=(callback,),
            daemon=True
        )

        thread.start()

    #######################################################

    def shutdown(self):

        self.running = False

        self.engine.stop()

        print("[Voice] Shutdown")
