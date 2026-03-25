# 🎤 Speech-to-Text Web Application

A full-stack AI-powered Speech-to-Text (STT) web application that converts audio into text using **SpeechRecognition** and a **FastAPI backend**, with a clean and modern frontend UI.

---

## 🚀 Features

* 🎧 Transcribe audio from `.wav` files
* 🎤 Live microphone speech recognition (CLI)
* 🔁 Continuous listening with voice stop command ("stop")
* ⚡ FastAPI backend with REST API
* 🌐 Frontend UI with file upload and real-time transcription
* 💬 Live status updates (Processing, Success, Errors)
* 🎨 Smooth UI with pastel theme + animations
* 💾 Option to save transcription to file
* 🛡️ Error handling (timeout, API errors, invalid input)

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SpeechRecognition
* PyAudio

### Frontend

* HTML
* CSS (Pastel UI + animations)
* JavaScript (Fetch API)

---

## 📂 Project Structure

```bash
Speech-to-Text/
│
├── speech_to_text.py      # FastAPI app + STT logic
├── frontend/
│   ├── index.html        # UI layout
│   ├── style.css         # Styling + animations
│   └── script.js         # Frontend logic + API calls
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/roshini0108/speech-to-text-system.git
cd speech-to-text-system
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 🖥️ Start Backend (FastAPI)

```bash
uvicorn speech_to_text:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

### 🌐 Open Frontend

Open in browser:

```text
frontend/index.html
```

---

## 🔗 API Endpoint

### POST `/transcribe`

* Accepts: `.wav` audio file
* Returns:

```json
{
  "success": true,
  "text": "Transcribed speech here"
}
```

---

## 🎧 Usage

### 🔹 Upload Audio File

1. Select `.wav` file from UI
2. Wait for processing
3. View transcription in output box

---

### 🔹 Microphone (CLI Mode)

```bash
python speech_to_text.py
```

* Choose microphone option
* Speak continuously
* Say **"stop"** to finish

---

## ⚠️ Notes

* Use `.wav` format for best results
* Ensure microphone permissions are enabled
* Internet connection required (Google Speech API)
* Accuracy depends on audio clarity

---

## 🌟 Future Improvements

* 🎤 Microphone support in web UI
* 📁 Support for `.mp3` and other formats
* ☁️ Deployment (Render / Vercel)
* 🧠 Advanced models (Wav2Vec)

---

## 👩‍💻 Author

**Roshini Mutyala**
B.Tech CSE | AI & Web Development

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
