# movie_recommender_app.py

import os
import asyncio
import logging
import streamlit as st
from dotenv import load_dotenv

from pilottai import Pilott
from pilottai.core import LLMConfig
from pilottai.agent import Agent

# ------------------------------------------------------------------------------
# ✅ Configuration & Setup
# ------------------------------------------------------------------------------

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set logging level
logging.basicConfig(level=logging.INFO)

# ------------------------------------------------------------------------------
# 🚀 Core Function to Run PilottAI
# ------------------------------------------------------------------------------

async def run_movie_recommender(genre: str, language: str) -> str:
    """
    Run the PilottAI framework with a movie recommendation agent.

    Args:
        genre (str): Movie genre.
        language (str): Preferred language.

    Returns:
        str: List of recommended movies.
    """
    llm_config = LLMConfig(
        model_name="o3-mini-2025-01-31",
        provider="openai",
        api_key=OPENAI_API_KEY,
        temperature=1.0,
    )

    movie_agent = Agent(
        role="Movie Recommender",
        goal="Suggest 5 movie titles based on user's genre and language preference.",
        description="Expert in recommending movies based on genre and language.",
        tasks=f"Recommend {language} {genre} movies",
        llm_config=llm_config,
        memory_enabled=True,
    )

    pilott = Pilott(agents=[movie_agent], llm_config=llm_config)
    results = await pilott.serve()
    print(results[0].output)
    return results[0].output if results else "No recommendations found."
    
# ------------------------------------------------------------------------------
# 🎯 Streamlit User Interface
# ------------------------------------------------------------------------------

def main():
    st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")
    st.title("🎬 Movie Recommender")
    st.markdown("An AI-powered movie suggestion app built with [PilottAI](https://pilottai.com/)")

    genre = st.selectbox("Choose a movie genre:", ["", "Action", "Romantic", "Comedy", "Horror", "Drama"])
    language = st.selectbox("Choose a language:", ["", "English", "Kannada", "Tamil", "Telugu", "Hindi"])

    if st.button("Get Recommendations"):
        if genre and language:
            with st.spinner("Thinking... 🤖🍿"):
                try:
                    recommendations = asyncio.run(run_movie_recommender(genre, language))
                    st.success("Here are your movie suggestions:")
                    st.code(recommendations, language="markdown")
                except Exception as e:
                    logging.exception("Error during movie recommendation:")
                    st.error("Something went wrong while generating recommendations. Please try again.")
        else:
            st.warning("Please select both a genre and a language.")

# ------------------------------------------------------------------------------
# 📌 Entry Point
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
