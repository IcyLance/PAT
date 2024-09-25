import google.generativeai as genai
from dotenv import load_dotenv
from openai import OpenAI
import os

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

    print(chat_completion.choices[0].message)

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

    print(chat_completion.choices[0].message)

def gem_f(q):

    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    response = model.generate_content(q)

    print('\n')
    print(response.text)
    print('\n')

def gem_p(q):

    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    response = model.generate_content(q)

    print('\n')
    print(response.text)
    print('\n')

comp_names = list()

def sani(question):

    # load file with company names to check against the question
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'list.txt')
    f = open(file_path, 'r')

    # read the file line by line
    comp_name = f.readline()
    while(comp_name):
        comp_name = comp_name.strip() # strip white spaces from ends
        question = question.replace(comp_name, 'example-company') #replace the found strings with 'example-company'
        comp_names.append(comp_name) #store the company name to later replace back in before output
        comp_name = f.readline()
    f.close()
    return question

def unsani(answer):
    for name in comp_names:
        answer = answer.replace('example-company', name)
        comp_names.pop()
    return answer

def check_sani_q(question):

    while(True):
        print('Sanitized input:\n' + question + '\n')
        yes_no = input("Specify more sanitizing? (yes/no): ")
        if yes_no.lower() == "yes":
            add_sani_word = input("Word/phrase to remove: ")
            add_sani_word = add_sani_word.strip()
            question = question.replace(add_sani_word, "example-company")
        elif yes_no.lower() == 'no':
            break
        else:
            print("\nInvalid input. Enter 'yes' or 'no'\n")
