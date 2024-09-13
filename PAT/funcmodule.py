import google.generativeai as genai
from dotenv import load_dotenv
import os

def gem(q):

    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')

    print('\n')
    response = model.generate_content(q)
    print(response.text)
    print('\n')


def sanitize(in_q):

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'list.txt')
    f = open(file_path, 'r')
    word = f.readline()
    out_q = in_q
    while(word):
        word = word.strip()

        out_q = out_q.replace(word, 'example-company')

        word = f.readline()
    f.close()
    return out_q