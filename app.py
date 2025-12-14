import streamlit as st
from crew import run_pipeline
import os

st.set_page_config(
    page_title="YouTube to Blog Generator",
    layout="centered"
)

st.title(" YouTube to Blog Generator")
st.write(
    "Paste a YouTube video link and this app will generate a professional blog post from it."
)

youtube_url = st.text_input(" Enter YouTube Video URL")
topic = st.text_input(" Topic (optional)", value="YouTube Video Content")

word_count = st.number_input(
    " Desired Blog Length (words)",
    min_value=300,
    max_value=3000,
    value=800,
    step=100
)

if st.button("Generate Blog"):
    st.session_state.clear()

    if not youtube_url.strip():
        st.error("Please enter a valid YouTube URL.")
    else:
        with st.spinner("Analyzing video and generating blog..."):
            try:
                result = run_pipeline(
                    youtube_url=youtube_url,
                    topic=topic,
                    word_count=word_count
                )

                st.session_state["last_blog_file"] = result["blog_file"]
                st.session_state["video_summary"] = result["summary"]

            except Exception as e:
                st.error(str(e))

if "video_summary" in st.session_state:
    st.subheader(" Video Summary")
    st.write(st.session_state["video_summary"])
    st.divider()

if "last_blog_file" in st.session_state:
    blog_path = st.session_state["last_blog_file"]

    if os.path.exists(blog_path):
        with open(blog_path, "r", encoding="utf-8-sig", errors="replace") as f:
            blog_content = f.read()

        st.success("Blog generated successfully!")
        st.markdown(blog_content)

        st.download_button(
            label="Download Blog (.md)",
            data=blog_content,
            file_name=blog_path,
            mime="text/markdown"
        )
