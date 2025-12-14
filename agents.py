from crewai import Agent
import os
import streamlit as st


os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_API_BASE"]
os.environ["OPENAI_MODEL_NAME"] = "llama-3.1-8b-instant"


blog_researcher = Agent(
    role="Content Researcher",
    goal="Analyze the provided video content and extract key insights.",
    verbose=True,
    memory=False,
    backstory="You extract factual, structured information only from the given content.",
    allow_delegation=False
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Write a professional blog based on the research summary.",
    verbose=True,
    memory=False,
    backstory="You write clean, professional blog articles with clear attribution.",
    allow_delegation=False
)
