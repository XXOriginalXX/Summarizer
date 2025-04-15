# 📺 YouTube Video Summarizer

This is a simple yet powerful **YouTube Video Summarizer App** built using **Streamlit**, **OpenAI's Whisper**, and **Hugging Face Transformers**. It allows users to input a YouTube video URL and receive a **concise summary** of the video content — either from subtitles (if available) or from transcribed audio.

---

## 🚀 Features

- 🔗 Input any YouTube video URL
- 📝 Extract subtitles (if available)
- 🎙️ Transcribe audio using OpenAI's Whisper (if no subtitles)
- 🧠 Summarize content using Hugging Face’s BART model
- 🖼️ Simple, interactive UI with Streamlit

-

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – For frontend UI
- **Pytube** – For downloading YouTube videos
- **MoviePy** – For audio extraction
- **Whisper** – For speech-to-text transcription
- **Hugging Face Transformers API** – For text summarization
- **YouTube Transcript API** – For fetching subtitles

---

## 📦 Installation

### Prerequisites

Make sure you have Python 3.7+ and `ffmpeg` installed.

### Step-by-step

```bash
# Clone the repo
git clone https://github.com/yourusername/youtube-video-summarizer.git
cd youtube-video-summarizer

# Install dependencies
pip install -r requirements.txt
```
## 🔑 Hugging Face API Key
You will need a Hugging Face API key to access the summarization model.

Go to https://huggingface.co and sign in or create an account.

Get your access token from https://huggingface.co/settings/tokens.

Replace "YOUR_HUGGINGFACE_API_KEY" in the code with your actual token.
