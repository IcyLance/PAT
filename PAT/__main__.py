from .funcmodule import gem, sanitize
import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Choose an AI model you want to use. ***Please be sure you have obtained the corresponding API key***.
    """

# @app.command()
# def main(model: str):
#     raw_q = ''
#     sani_q = ''
#     while(raw_q != 'q'):
#         raw_q = input('Input: ').strip()
#         sani_q = sanitize(raw_q)
#         if(raw_q == 'q'):
#             return
#         elif(raw_q == ''):
#             print("Input required\n")
#         elif(model == 'gemini'):
#             # gem(sani_q)
#             print("gemini\n")
#         else:
#             print('Please choose a model')

@app.command()
def gemini():
    """
    Gemini-1.5-flash. Takes your question as INPUT after program start
    """

    question = ''
    question = input('Input: ').strip()
    if(question == 'q'):
        return
    elif(question == ''):
        print("Input required\n")
    else:
        gem(question)