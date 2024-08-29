import google.generativeai as genai
from dotenv import load_dotenv, dotenv_values
import os
import sys

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

question = sys.argv[1]

response = model.generate_content(question)
print(response.text)