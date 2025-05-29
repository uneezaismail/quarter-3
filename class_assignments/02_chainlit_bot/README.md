# Gemini Chatbot 🤖

A simple chatbot interface built with **Chainlit** and **Google Gemini API**, powered by **Python**.

##  Features

- Interactive chat powered by Gemini 2.0 Flash model
- Built with Chainlit for a sleek UI
- Loads environment variables securely using `dotenv`

##  Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/uneezaismail/02-chainlit-bot.git
   cd 02-chainlit-bot
   ```

2. **Install dependencies:**

Run the following command:

```python
pip install -r requirements.txt
```

3. **Create a .env file in the project root:**

Add your Gemini API Key like this:

```python
GEMINI_API_KEY=your_api_key_here
```

4. **Run the chatbot:**

Use this command to start the app:

```python
chainlit run main.py
```

##  Tech Stack

-  **Python** – The core language used for development.
-  **Chainlit** – Framework for building conversational UIs.
-  **Google Generative AI** – Powers the chatbot with Gemini 2.0 Flash.
-  **Dotenv** – Manages and secures environment variables.
