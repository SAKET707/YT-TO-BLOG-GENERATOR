#  YouTube to Blog Generator
---
##  **Live App:**  
https://yt-to-blog-generator-by-saket.streamlit.app/

---

##  Overview

**YouTube to Blog Generator** is a GenAI-powered web application that converts YouTube videos into:

-  A **concise video summary**
-  A **professionally written blog article** with controllable length

The app extracts video transcripts, performs structured research, and generates high-quality written content using **CrewAI agents** and **LLMs** — all through a simple Streamlit interface.

---

##  Features

-  Paste any YouTube video link
-  Automatically extracts transcript + metadata
-  Generates a **clean summary paragraph** of the video
-  Generates a **full-length blog post**
-  User-controlled blog length (word count)
-  No promotions, links, or YouTube mentions in output
-  Download blog as a Markdown file
-  Deployed on Streamlit Cloud

---

##  Architecture

The pipeline follows a **stateless, sequential GenAI workflow**:

1. **Transcript Extraction**
   - Uses `youtube-transcript-api`
   - Falls back to video description if transcript is unavailable

2. **Research Agent**
   - Analyzes raw video content
   - Extracts key ideas and explanations
   - Produces a structured research summary

3. **Summary Generation**
   - Creates a concise, neutral summary paragraph
   - Based strictly on research output

4. **Blog Writer Agent**
   - Converts research into a professional blog article
   - Enforces word-count constraints
   - Attributes ideas to the creator

5. **Output Handling**
   - UTF-8 safe writing (Unicode-friendly)
   - Streamlit UI display + download

---

##  Demo

This demo shows the **YouTube to Blog Generator** in action using the following video:

 **YouTube Video Used:**  
https://youtu.be/zo7i8VTpfNM?si=U5MGRPdPDkl3Hu_6

> **Credit:** All original video content and ideas belong to the respective creator, **MrBeast**.  
> This project only analyzes publicly available content for educational and demonstration purposes.

The screenshots below illustrate the end-to-end workflow:
- Generating a concise summary
- Producing a full-length blog article

|                          |                         |                       |
|--------------------------|-------------------------|-----------------------|
| <img src="https://github.com/user-attachments/assets/c8f0e239-9c0c-4514-8b1f-acb86e4fb87f" width="280" /> | <img src="https://github.com/user-attachments/assets/71489015-3cf9-4913-8816-d330685bc8bd" width="280" /> | <img src="https://github.com/user-attachments/assets/3b6c03c1-b78e-455c-808e-8cbc6aa81eb2" width="280" /> |


##  Tech Stack

- **Python**
- **Streamlit**
- **CrewAI**
- **LLMs**
- youtube-transcript-api
- yt-dlp

---

##  Future Improvements

  - Batch processing (multiple YouTube URLs)
  - Social media post generation (LinkedIn / Twitter)
  - PDF / DOCX export
  - API version (FastAPI backend)
