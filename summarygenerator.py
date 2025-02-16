import os
import pytube
import whisper
import requests
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from moviepy.editor import AudioFileClip

def download_video(video_url, output_path="downloads"):
    yt = pytube.YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download(output_path)
    return output_file

def extract_audio(video_path):
    audio_path = video_path.replace(".mp4", ".mp3")
    clip = AudioFileClip(video_path)
    clip.write_audiofile(audio_path)
    return audio_path

def get_subtitles(video_url):
    video_id = video_url.split("v=")[-1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t["text"] for t in transcript])
        return text
    except (TranscriptsDisabled, NoTranscriptFound):
        return None

def transcribe_audio(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    return result["text"]

def generate_summary(text):
    api_key = "YOUR_HUGGINGFACE_API_KEY"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": text, "parameters": {"max_length": 200, "min_length": 50, "do_sample": False}}
    response = requests.post("https://api-inference.huggingface.co/models/facebook/bart-large-cnn", headers=headers, json=payload)
    return response.json()[0]["summary_text"]

st.title("YouTube Video Summarizer")
video_url = st.text_input("Enter YouTube Video URL")

if st.button("Summarize") and video_url:
    with st.spinner("Processing..."):
        video_path = download_video(video_url)
        audio_path = extract_audio(video_path)
        
       text = get_subtitles(video_url)
       if text is None or text.strip() == "":
           st.warning("No subtitles available. Transcribing audio...")
           text = transcribe_audio(audio_path)

        
        summary = generate_summary(text)
        st.subheader("Descriptive Summary:")
        st.write(summary)
        
        os.remove(video_path)
        os.remove(audio_path)
