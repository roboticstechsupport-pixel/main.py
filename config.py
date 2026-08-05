"""
==========================================================
Project ULTRON
Configuration File
==========================================================
"""

from pathlib import Path
import os


class Config:
    """
    Global configuration for Project ULTRON.
    """

    def __init__(self):

        # --------------------------------------------------
        # General
        # --------------------------------------------------
        self.ASSISTANT_NAME = "ULTRON"
        self.VERSION = "1.0.0"

        # --------------------------------------------------
        # Base Directories
        # --------------------------------------------------
        self.BASE_DIR = Path(__file__).resolve().parent

        self.DATA_DIR = self.BASE_DIR / "data"
        self.LOG_DIR = self.DATA_DIR / "logs"
        self.MODEL_DIR = self.BASE_DIR / "models"
        self.ASSETS_DIR = self.BASE_DIR / "assets"

        # Create folders automatically
        self.DATA_DIR.mkdir(exist_ok=True)
        self.LOG_DIR.mkdir(exist_ok=True)
        self.MODEL_DIR.mkdir(exist_ok=True)
        self.ASSETS_DIR.mkdir(exist_ok=True)

        # --------------------------------------------------
        # Database
        # --------------------------------------------------
        self.DATABASE_PATH = self.DATA_DIR / "memory.db"

        # --------------------------------------------------
        # AI Settings
        # --------------------------------------------------
        self.LLM_PROVIDER = "ollama"       # "ollama" or "openai"
        self.LLM_MODEL = "llama3.1:8b"

        # OpenAI API Key (if used)
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

        # --------------------------------------------------
        # Voice
        # --------------------------------------------------
        self.ENABLE_VOICE = True
        self.WAKE_WORD = "ultron"

        self.SPEECH_RATE = 170
        self.SPEECH_VOLUME = 1.0

        # --------------------------------------------------
        # Vision
        # --------------------------------------------------
        self.ENABLE_CAMERA = True
        self.CAMERA_INDEX = 0

        self.FRAME_WIDTH = 1280
        self.FRAME_HEIGHT = 720

        # --------------------------------------------------
        # UI
        # --------------------------------------------------
        self.THEME = "dark"

        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 750

        # --------------------------------------------------
        # Logging
        # --------------------------------------------------
        self.LOG_LEVEL = "INFO"

        # --------------------------------------------------
        # Automation
        # --------------------------------------------------
        self.ENABLE_AUTOMATION = True

        # --------------------------------------------------
        # Internet
        # --------------------------------------------------
        self.ENABLE_INTERNET = True

        # --------------------------------------------------
        # Personality
        # --------------------------------------------------
        self.PERSONALITY = (
            "You are ULTRON, a futuristic AI assistant. "
            "Be intelligent, concise, helpful, and professional. "
            "Do not claim abilities you do not have."
        )

        # --------------------------------------------------
        # Startup Greeting
        # --------------------------------------------------
        self.STARTUP_MESSAGE = (
            "System initialized. ULTRON is now online."
        )

    # ======================================================
    # Utility Methods
    # ======================================================

    def summary(self):
        """
        Print a summary of the current configuration.
        """

        print("=" * 50)
        print("PROJECT ULTRON CONFIGURATION")
        print("=" * 50)
        print(f"Assistant : {self.ASSISTANT_NAME}")
        print(f"Version   : {self.VERSION}")
        print(f"Model     : {self.LLM_MODEL}")
        print(f"Provider  : {self.LLM_PROVIDER}")
        print(f"Voice     : {self.ENABLE_VOICE}")
        print(f"Camera    : {self.ENABLE_CAMERA}")
        print(f"Database  : {self.DATABASE_PATH}")
        print("=" * 50)
