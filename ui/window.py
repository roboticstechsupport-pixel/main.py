"""
==========================================================
Project ULTRON
UI Window
==========================================================
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QApplication
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class UltronWindow(QMainWindow):

    def __init__(self, ultron):

        super().__init__()

        self.ultron = ultron

        self.setWindowTitle("PROJECT ULTRON")

        self.resize(
            ultron.config.WINDOW_WIDTH,
            ultron.config.WINDOW_HEIGHT
        )

        self.build_ui()

    ########################################################

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        ####################################################
        # Title
        ####################################################

        title = QLabel("PROJECT ULTRON")

        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Arial", 22))

        title.setStyleSheet("""
            QLabel{
                color:#00FFFF;
                font-weight:bold;
            }
        """)

        layout.addWidget(title)

        ####################################################
        # Status
        ####################################################

        self.status = QLabel("Status : ONLINE")

        self.status.setStyleSheet("""
            QLabel{
                color:#00FF00;
                font-size:14px;
            }
        """)

        layout.addWidget(self.status)

        ####################################################
        # Chat Window
        ####################################################

        self.chat = QTextEdit()

        self.chat.setReadOnly(True)

        self.chat.setStyleSheet("""
            QTextEdit{
                background:#111111;
                color:white;
                border:2px solid #00FFFF;
                font-size:15px;
            }
        """)

        layout.addWidget(self.chat)

        ####################################################
        # Input
        ####################################################

        row = QHBoxLayout()

        self.input = QLineEdit()

        self.input.setPlaceholderText(
            "Type your message..."
        )

        self.input.returnPressed.connect(
            self.send_message
        )

        row.addWidget(self.input)

        ####################################################
        # Send Button
        ####################################################

        self.send_btn = QPushButton("Send")

        self.send_btn.clicked.connect(
            self.send_message
        )

        row.addWidget(self.send_btn)

        ####################################################
        # Voice Button
        ####################################################

        self.voice_btn = QPushButton("🎤")

        self.voice_btn.clicked.connect(
            self.listen_voice
        )

        row.addWidget(self.voice_btn)

        layout.addLayout(row)

        ####################################################
        # Theme
        ####################################################

        self.setStyleSheet("""

            QMainWindow{
                background:#050505;
            }

            QLineEdit{
                background:#202020;
                color:white;
                border:2px solid cyan;
                padding:6px;
            }

            QPushButton{

                background:#00AEEF;

                color:white;

                font-weight:bold;

                border-radius:6px;

                padding:8px;
            }

            QPushButton:hover{

                background:#0090C5;

            }

        """)

        self.add_message(
            "ULTRON",
            "System initialized."
        )

    ########################################################

    def add_message(self, sender, text):

        self.chat.append(
            f"<b>{sender}:</b> {text}<br>"
        )

    ########################################################

    def send_message(self):

        text = self.input.text().strip()

        if not text:
            return

        self.add_message("YOU", text)

        self.input.clear()

        try:

            reply = self.ultron.assistant.ask(text)

        except Exception as e:

            reply = str(e)

        self.add_message("ULTRON", reply)

    ########################################################

    def listen_voice(self):

        self.status.setText(
            "Status : Listening..."
        )

        QApplication.processEvents()

        text = self.ultron.voice.listen()

        self.status.setText(
            "Status : ONLINE"
        )

        if not text:
            return

        self.add_message("YOU", text)

        reply = self.ultron.assistant.ask(text)

        self.add_message("ULTRON", reply)

        self.ultron.voice.speak_async(reply)
