from crewai import Crew, Process, Task
from agents import blog_researcher, blog_writer
from tools import yt_tool
import uuid
import re


def clean_text(text: str) -> str:
    text = re.sub(r'\$+', '', text)
    text = re.sub(r'[^\w\s.,!?()-]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def run_pipeline(youtube_url: str, topic: str, word_count: int):

    raw_content = yt_tool(youtube_url)
    video_content = clean_text(raw_content)

    if len(video_content) < 500:
        raise ValueError("Insufficient video content to generate a blog.")

    creator_name = "the creator"
    for line in raw_content.splitlines():
        if line.startswith("Channel:"):
            creator_name = line.replace("Channel:", "").strip()
            break

    output_file = f"blog_{uuid.uuid4().hex[:8]}.md"

    research_task = Task(
        description=(
            "You are given the extracted content of a YouTube video below.\n\n"
            "VIDEO CONTENT:\n"
            "{video_content}\n\n"
            "Based ONLY on this content:\n"
            "- Extract the main ideas\n"
            "- Identify key explanations and concepts\n"
            "- Ignore promotions, links, playlists, and metadata\n"
        ),
        expected_output="A detailed structured research summary.",
        agent=blog_researcher
    )

    write_task = Task(
        description=(
            "Write a professional blog article using ONLY the research summary.\n\n"
            f"Length Requirement:\n"
            f"- The blog must be approximately {word_count} words\n"
            f"- Acceptable range: {int(word_count * 0.9)}–{int(word_count * 1.1)} words\n\n"
            "Attribution Rule:\n"
            "- Attribute the ideas to {creator_name} in the introduction\n\n"
            "Rules:\n"
            "- Do NOT mention YouTube\n"
            "- Do NOT include promotions or links\n"
            "- Explain the topic clearly and professionally\n"
        ),
        expected_output=(
            f"A complete professional blog article of around {word_count} words "
            "with an introduction, structured sections, and a concise conclusion."
        ),
        agent=blog_writer
    )
    summary_task = Task(
        description=(
            "Using ONLY the research summary, write a concise overview of the video.\n\n"
            "Rules:\n"
            "- 120–180 words\n"
            "- Neutral, factual tone\n"
            "- No YouTube mentions\n"
            "- No promotions\n"
            "- No bullet points\n"
            "- Single cohesive paragraph"
        ),
        expected_output="A concise, well-written summary paragraph.",
        agent=blog_researcher
    )


    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[
            research_task,
            summary_task,
            write_task
        ],
        process=Process.sequential,
        memory=False,
        cache=False
    )


    crew.kickoff(
        inputs={
            "topic": topic,
            "video_content": video_content,
            "creator_name": creator_name
        }
    )

    summary_output = ""
    if summary_task.output:
        summary_output = (
            getattr(summary_task.output, "raw_output", None)
            or getattr(summary_task.output, "text", None)
            or str(summary_task.output)
        )

    blog_output = ""
    if write_task.output:
        blog_output = (
            getattr(write_task.output, "raw_output", None)
            or getattr(write_task.output, "text", None)
            or str(write_task.output)
        )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(blog_output)

    return {
        "blog_file": output_file,
        "summary": summary_output
    }


