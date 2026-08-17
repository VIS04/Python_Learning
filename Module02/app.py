from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY")) #create an object in the class(API key obtained from .env file)

while True:
    user_input = input ("\n You :")

    if user_input.lower()=="exit":
        break
    response= client.responses.create(
        model = "gpt-5-mini",
        input = user_input
    )
    print("\n GPT:", response.output_text)