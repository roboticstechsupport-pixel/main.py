"""
==========================================================
 Project ULTRON
 AI Desktop Assistant
 Author : Your Name
 Version: 1.0.0
==========================================================
"""

import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication

from config import Config
from ai.assistant import Assistant
from speech.voice import VoiceEngine
from vision.camera import VisionSystem
from ui.window import UltronWindow


class Ultron:

    def __init__(self):

        print("=" * 60)
        print("        PROJECT ULTRON INITIALIZING")
        print("=" * 60)

        self.config = Config()

        print("[✓] Configuration Loaded")

        self.assistant = Assistant(self.config)

        print("[✓] AI Loaded")

        self.voice = VoiceEngine(self.config)

        print("[✓] Voice Engine Loaded")

        self.vision = VisionSystem(self.config)

        print("[✓] Vision Module Loaded")

        self.window = UltronWindow(self)

        print("[✓] UI Loaded")

    ########################################################

    def start(self):

        print("\nSystem Online")
        print("--------------------------")
        print("Time :", datetime.now().strftime("%H:%M:%S"))
        print("Assistant :", self.config.ASSISTANT_NAME)
        print("--------------------------")

        self.assistant.initialize()

        self.voice.initialize()

        self.vision.initialize()

        self.window.show()

    ########################################################

    def shutdown(self):

        print("\nShutting Down...")

        self.voice.shutdown()

        self.vision.shutdown()

        self.assistant.shutdown()

        print("Goodbye.")


###############################################################


def main():

    app = QApplication(sys.argv)

    ultron = Ultron()

    ultron.start()

    exit_code = app.exec()

    ultron.shutdown()

    sys.exit(exit_code)


###############################################################

if __name__ == "__main__":
    main()
