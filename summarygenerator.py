import streamlit as st
from pytube import YouTube

def download_subtitles(url):
    try:
        yt = YouTube(url)
        caption = yt.captions.get_by_language_code('en')  # English subtitles
        if caption:
            return caption.generate_srt_captions()
        else:
            return "No subtitles available for this video."
    except Exception as e:
        return f"Error: {e}"

st.title("YouTube Video Summarizer")

video_url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Summary"):
    if video_url:
        subtitles = download_subtitles(video_url)
        st.text_area("Extracted Subtitles", subtitles, height=300)
    else:
        st.warning("Please enter a valid YouTube URL.")
