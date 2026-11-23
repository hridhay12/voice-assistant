# voice-assistant
A lightweight Python voice assistant built with SpeechRecognition and pyttsx3 for real-time voice commands and offline text-to-speech responses.

# Python Desktop Voice Assistant

A lightweight desktop voice assistant built in Python using `SpeechRecognition` and `pyttsx3`. It listens to real-time voice commands, adjusts for ambient background noise, and responds using offline text-to-speech synthesis.

## Features

- **Offline Text-to-Speech:** Powered by `pyttsx3` (configured at 170 WPM) for fast, offline vocal responses.
- **Voice Command Recognition:** Uses Google Speech Recognition (`en-in` locale) with automatic ambient noise calibration and a 5-second listening window.
- **System & Web Automation Ready:** Includes built-in support for `os`, `datetime`, `time`, and `requests` to handle local tasks, time queries, and web API calls.

## Prerequisites

Before setting this up on another device, make sure the machine has:

- **Python 3.10 – 3.12** (recommended for smooth `PyAudio` wheel compatibility; newer versions like 3.14 may require compiling `PyAudio` from source).
- A working **microphone** and **speakers/headphones**.
- An active **internet connection** (required by Google's Speech Recognition API).

## Setup on Another Device

### 1. Download the Project
Clone the repository from GitHub (or download and extract the ZIP) and open the project folder in your terminal:

```bash
cd python-voice-assistant
```
2. Create a Virtual Environment (Recommended)
Isolating dependencies prevents version conflicts with other Python projects on the device.
Windows (PowerShell):
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```
macOS / Linux:
```
Bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
Install the required Python packages:
```
python -m pip install pyttsx3 SpeechRecognition pyaudio requests

```
4. Run the Assistant

```
Bash
python assistant.py

```
Speak clearly into your microphone once you see LISTENING... in the terminal.



Troubleshooting
PyAudio fails to install:
    
    Windows: Ensure you are using Python 3.10–3.12, or install via Anaconda (conda install pyaudio).
    
    macOS: Install PortAudio first using Homebrew (brew install portaudio), then run pip install pyaudio.
    
    Linux (Ubuntu/Debian): Run sudo apt-get install portaudio19-dev python3-pyaudio before installing with pip.

ModuleNotFoundError in VS Code: If you have multiple Python installations (such as Anaconda and standalone Python), press Ctrl + Shift + P -> Python: Select Interpreter and choose the environment where you installed the packages.

Microphone not detected: Check your OS privacy settings to ensure terminal/IDE apps have permission to access the microphone.
