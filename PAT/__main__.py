import google.generativeai as genai
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    genai.configure(api_key=os.getenv("API_KEY"))

    model = genai.GenerativeModel('gemini-1.5-flash')

    question = ""
    convo = ''
    while(question != 'q'):
        question = input('Input: ')
        if(question != 'q'):
            print('\n')
            response = model.generate_content(question + convo)
            print(response.text)
            print('\n')
            convo += question + '. '
