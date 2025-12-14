
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
import re


def extract_video_id(url: str) -> str:
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"youtube\.com/embed/([a-zA-Z0-9_-]{11})"
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    raise ValueError("Invalid YouTube URL")


def yt_tool(youtube_url: str) -> str:
    video_id = extract_video_id(youtube_url)

    transcript_text = ""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([t["text"] for t in transcript])
    except Exception:
        pass

    ydl_opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)

    return f"""
Title: {info.get("title", "")}
Channel: {info.get("uploader", "")}
Duration: {info.get("duration", 0)}

Content:
{transcript_text or info.get("description", "")}
""".strip()
