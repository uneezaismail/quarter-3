import os 
import chainlit as cl  
import google.generativeai as genai  
from dotenv import load_dotenv  

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API with the API key
genai.configure(api_key=gemini_api_key)

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")


# chainlit decorator for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():
   
    await cl.Message(content="Hello! how can I help you?").send()


# chainlit decorator for when a new message is received
@cl.on_message
async def handle_message(message: cl.Message):
    # Get the message from user
    prompt = message.content

    # Generate response
    response = model.generate_content(prompt)

    # Extract text from response, or empty string if no text
    response_text = response.text if hasattr(response, "text") else ""

    # Send response back to user
    await cl.Message(content=response_text).send()