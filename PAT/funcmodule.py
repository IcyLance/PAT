import google.generativeai as genai
from dotenv import load_dotenv
import os

def gem(q):

    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    q = sanitize(q)
    response = model.generate_content(q)

    print('\n')
    print(response.text)
    print('\n')

comp_names = list()

def sanitize(question):

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

def unsanitize(answer):
    for name in comp_names:
        answer = answer.replace('example-company', name)
        comp_names.pop()
    return answer