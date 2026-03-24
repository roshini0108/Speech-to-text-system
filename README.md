# 🎤 Speech-to-Text System

A Python-based Speech-to-Text (STT) application that converts spoken audio into text using the SpeechRecognition library and Google Speech API.

---

## 🚀 Features

* 🎧 Transcribe audio from `.wav` files
* 🎤 Live microphone speech recognition
* 🔁 Continuous listening mode
* 🛑 Stop recording using voice command ("stop") or Ctrl+C
* ⏱ Handles silence and timeouts
* 💾 Save transcription to `output.txt`
* ⚡ Real-time feedback ("You said: ...")

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* PyAudio (for microphone input)

---

## 📂 Project Structure

```id="9bx0c4"
Speech-to-Text/
│
├── speech_to_text.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash id="8gq3hc"
git clone https://github.com/your-username/speech-to-text.git
cd speech-to-text
```

---

### 2. Create virtual environment

```bash id="y5r3wo"
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash id="nwh8j1"
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the program

```bash id="o5yq1u"
python speech_to_text.py
```

---

### Choose input method

```text id="ec0tqb"
1. Audio file
2. Microphone
```

---

### 🎧 File input

Provide path to `.wav` file:

```text id="6fhz3r"
C:/Users/lenovo/Downloads/harvard.wav
```

---

### 🎤 Microphone input

* Speak continuously
* Say **"stop"** to end recording

---

### 💾 Save output

```text id="3jrsn3"
Save transcription to output.txt? (y/n)
```

---

## ⚠️ Notes

* Ensure microphone permissions are enabled
* Use clear audio for better accuracy
* Internet connection required for Google API

---

## 👩‍💻 Author

Roshini Mutyala
B.Tech CSE | AI & Web Development

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
