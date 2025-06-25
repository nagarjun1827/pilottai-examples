import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
import logging

from pilottai import Pilott
from pilottai.core import LLMConfig
from pilottai.agent import Agent
from pilottai.core.task import Task

# -----------------------------------
# 🔧 Setup Logging & Environment
# -----------------------------------
logging.basicConfig(level=logging.WARNING)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# -----------------------------------
# 🧠 Caching LLM Config & Agent Setup
# -----------------------------------
@st.cache_resource
def get_llm_config() -> LLMConfig:
    """
    Returns a cached LLM configuration for PilottAI using OpenAI.
    """
    return LLMConfig(
        model_name="o3-mini-2025-01-31",
        provider="openai",
        api_key=OPENAI_API_KEY,
        temperature=1
    )

def get_agent(llm_config: LLMConfig, task: Task) -> Agent:
    """
    Creates a new agent with the provided task and LLM configuration.

    Args:
        llm_config (LLMConfig): The configuration for the LLM.
        task (Task): The main task the agent should perform.

    Returns:
        Agent: Configured PilottAI agent.
    """
    return Agent(
        role="Movie Recommender",
        goal="Suggest 5 movie titles based on user's choice of genre",
        description="You are expert in suggesting movie titles",
        tasks=task,
        llm_config=llm_config,
        memory_enabled=True
    )

# -----------------------------------
# 🚀 Async Execution Logic
# -----------------------------------
async def run_pilott(genre: str, language: str) -> str:
    """
    Run a PilottAI agent to recommend 5 movies based on genre and language.

    Args:
        genre (str): Movie genre selected by user (e.g., Action, Comedy)
        language (str): Language selected by user (e.g., Kannada, Hindi)

    Returns:
        str: AI-generated list of recommended movies
    """
    try:
        llm_config = get_llm_config()
        task = Task(description=f"Recommend {language} {genre} movies")
        agent = get_agent(llm_config, task)

        result = await Pilott(
            agents=[agent],
            llm_config=llm_config
        ).serve()

        return result[0].output

    except Exception as e:
        return f"❌ Error: {str(e)}"

# -----------------------------------
# 🌐 Streamlit UI
# -----------------------------------
st.set_page_config(page_title="AI Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommender")
st.markdown("An AI-powered **Movie Recommender** that suggests 5 movies based on your preferred genre and language.")

# Dropdown selections
genre = st.selectbox("🎭 Choose a movie genre:", ["", "Action", "Romantic", "Comedy", "Horror", "Drama"])
language = st.selectbox("🗣️ Choose a language:", ["", "English", "Kannada", "Tamil", "Telugu", "Hindi"])

# Button click
if st.button("🎥 Get Recommendations"):
    if genre and language:
        with st.spinner("🧠 Thinking..."):
            output = asyncio.run(run_pilott(genre, language))
            st.success("✅ Here are your movie suggestions:")
            st.code(output, language="markdown")
    else:
        st.warning("⚠️ Please select both a genre and a language.")
