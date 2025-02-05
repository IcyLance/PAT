import google.generativeai as genai
from dotenv import load_dotenv
from openai import OpenAI
import socket
import os
import re

def gpt_3(q):
    load_dotenv()
    client = OpenAI(
        api_key=os.getenv('GPT_API_KEY')
    )
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": q
            }
        ]   
    )

    return chat_completion.choices[0].message

def gpt_4(q):
    load_dotenv()
    client = OpenAI(
        api_key=os.getenv('GPT_API_KEY')
    )
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": q
            }
        ]   
    )

    return chat_completion.choices[0].message

def gem_f(q):

    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    response = model.generate_content(q)

    return response.text

def gem_p(q):

    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    response = model.generate_content(q)

    return response.text

def check_ipv6(s: str) -> bool:
    if not isinstance(s, str):
        return False
    try:
        socket.inet_pton(socket.AF_INET6, s)
        return True
    except socket.error:
        return False

def sani_ipv6(string: str) -> str:
    words = string.split()
    redacted_string = ["[REDACTED IPV6 ADDRESS]" if check_ipv6(word) else word for word in words]
    return " ".join(redacted_string)

def sani(question: str):

    # Remove sensitive patterns like emails and phone numbers
    question = sani_ipv6(question) # Remove IPV6 addresses. Was a bit more complex
    question = re.sub(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', '[REDACTED IPV4 ADDRESS]', question) # Remove IPV4 addresses
    question = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[REDACTED EMAIL]', question)  # Remove emails
    question = re.sub(r'(?:\+?\d{1,2}[\s\-]?)?(\(\d{1,3}\)[\s\-]?)?\d{1,4}[\s\-]?\d{1,4}[\s\-]?\d{1,4}', '[REDACTED PHONE]', question)  # Remove phone numbers

    # load file with company names to check against the question
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'list.txt')
    f = open(file_path, 'r')

    # read the file line by line
    comp_name = f.readline()
    while(comp_name):
        comp_name = comp_name.strip() # strip white spaces from ends
        question = question.lower()
        question = question.replace(comp_name.lower(), '[REDACTED COMPANY]') #replace the found strings'
        comp_name = f.readline()
    f.close()
    return question

def check_sani_q(question):
    while(True):
        print('Sanitized input:\n\n' + question + '\n')
        yes_no = input("Specify more sanitizing? (yes/No): ")
        if yes_no.lower() == "yes":
            add_sani_word = input("Word/phrase to remove: ")
            add_sani_word = add_sani_word.strip()
            replace_with = input("What to replace it with: ")
            question = question.replace(add_sani_word, replace_with)
        elif yes_no.lower() == 'no':
            break
        elif yes_no.lower() == '':
            break
        else:
            print("\nInvalid input. Enter 'yes' or 'no'\n")
