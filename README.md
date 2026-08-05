# 🤖 Project ULTRON

An AI-powered desktop assistant built with Python.

Project ULTRON is an original, open-source AI assistant inspired by futuristic computer assistants. It supports voice interaction, local AI models, computer vision, desktop automation, and a modern graphical interface.

> **Disclaimer**
>
> This project is an original creation inspired by science-fiction AI assistants. It is **not affiliated with or endorsed by Marvel**, and it does not reproduce copyrighted characters, artwork, or assets.

---

# Features

- 🎤 Voice Recognition
- 🔊 Text-to-Speech
- 🧠 AI Chat Assistant
- 👀 Webcam Vision
- 😊 Face Detection
- 📦 Object Detection
- 💻 Desktop Automation
- 🌐 Internet Search (optional)
- 💾 Conversation Memory
- 🖥️ Modern Desktop Interface
- ⚡ Modular Architecture

---

# Project Structure

```
Project-ULTRON/

├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── ai/
│   ├── assistant.py
│   ├── memory.py
│   └── llm.py
│
├── speech/
│   └── voice.py
│
├── vision/
│   └── camera.py
│
├── ui/
│   └── window.py
│
├── data/
│   └── memory.db
│
├── assets/
│
└── models/
```

---

# Requirements

- Python 3.11 or newer
- Windows, Linux, or macOS

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/Project-ULTRON.git
cd Project-ULTRON
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python main.py
```

---

# Recommended AI Backend

This project is designed to work with **Ollama**.

1. Install Ollama from https://ollama.com
2. Pull a supported model:

```bash
ollama pull llama3.1:8b
```

3. Start Ollama before launching the application.

---

# Technologies Used

- Python
- PySide6
- OpenCV
- SpeechRecognition
- pyttsx3
- Ollama
- SQLite
- PyAutoGUI

---

# Roadmap

## Phase 1

- [x] AI Chat
- [x] Voice Engine
- [ ] GUI
- [ ] Camera
- [ ] Memory

## Phase 2

- [ ] Face Recognition
- [ ] Object Detection
- [ ] Wake Word
- [ ] Plugin System

## Phase 3

- [ ] Smart Home Integration
- [ ] Mobile App
- [ ] Cloud Synchronization
- [ ] Multi-Agent Support

---

# Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

Please include clear descriptions and keep code style consistent.

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

# Acknowledgements

This project uses open-source software from the Python community, including:

- Python
- OpenCV
- PySide6
- Ollama
- SQLite

Thanks to all contributors to these projects.

---

# Contact

If you have ideas, improvements, or bug reports, please open a GitHub Issue or Pull Request.

---

## Project Status

🚧 **Under Active Development**

New features and improvements are planned as the project evolves.
