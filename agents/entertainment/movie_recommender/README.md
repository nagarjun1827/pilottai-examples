# 🎬 Movie Recommender using PilottAI + Streamlit

This project is an interactive **Streamlit** web app that uses [PilottAI](https://pilottai.com/) to recommend movies based on **user-selected genre and language**. The app utilizes a Large Language Model (LLM) via OpenAI to generate 5 relevant movie suggestions.

---

## 🚀 Features

- Recommends 5 movies based on selected **genre** and **language**
- Built with **Streamlit** for interactive web UI
- Powered by **PilottAI Agents**
- Simple, customizable, and easy to extend

---

## 📦 Tech Stack

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [PilottAI](https://pilottai.com/)
- [OpenAI API](https://platform.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/pygig/pilottai-examples.git <br>
cd movie_recommender

### 2. Create & Activate a Virtual Environment (Recommended)

python -m venv venv (On Windows) <br>
venv\Scripts\activate (On macOS/Linux) <br>
source venv/bin/activate <br>

### 3. Install Dependencies

pip install -r requirements.txt

**Note:** If requirements.txt is missing, you can install manually: <rb>
pip install streamlit python-dotenv pilottai

### 4. Configure Environment Variables
Create a .env file in the root directory:
touch .env

Add your OpenAI API key in .env:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
💡 Get your key from OpenAI API Keys

### 5. Run the Streamlit App

streamlit run app.py

## 🧠 How it Works
You choose a genre (e.g., Action, Comedy) and a language (e.g., Kannada, Hindi).

A PilottAI agent is created with a task like:
Recommend {language} {genre} movies

The agent uses OpenAI’s LLM to generate 5 relevant movie recommendations.

The results are displayed in a user-friendly Streamlit UI.

## 🛠️ Project Structure

```
movie_recommender/
├── .env/                           # Environment variables
├── movie_recommender.py/           # Main Streamlit app
├── requirements.txt/               # Python dependencies
├── README.md/                      # Project documentation
```

## 📝 License
This project is open-source and free to use. You may add a license (MIT, Apache 2.0, etc.) as per your needs.

## 🙋‍♂️ Support
If you face any issues or want to contribute:
Open an Issue or Submit a Pull Request
