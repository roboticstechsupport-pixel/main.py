"""
==========================================================
Project ULTRON
speech/wakeword.py
==========================================================
"""

import threading
import speech_recognition as sr


class WakeWordDetector:

    def __init__(self, wake_word="ultron"):

        self.wake_word = wake_word.lower()

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.running = False

    ##########################################################

    def initialize(self):

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

        self.running = True

        print(f"[WakeWord] Listening for '{self.wake_word}'")

    ##########################################################

    def listen_once(self):

        try:

            with self.microphone as source:

                audio = self.recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=4
                )

            text = self.recognizer.recognize_google(audio)

            print("[WakeWord] Heard:", text)

            return text.lower()

        except Exception:

            return ""

    ##########################################################

    def wait_for_wake_word(self):

        while self.running:

            text = self.listen_once()

            if self.wake_word in text:

                print("[WakeWord] Activated")

                return True

        return False

    ##########################################################

    def start(self, callback):

        def worker():

            while self.running:

                if self.wait_for_wake_word():

                    callback()

        threading.Thread(
            target=worker,
            daemon=True
        ).start()

    ##########################################################

    def stop(self):

        self.running = False
