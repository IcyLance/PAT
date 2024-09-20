from .funcmodule import gem, sani, check_sani_q
import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Choose an AI model you want to use. ***Please be sure you have obtained the corresponding API key***.
    """

@app.command()
def gemini(question: str, sanitize: bool = True, check: bool = True):
    """
    Gemini-1.5-flash.
    """
    if(question == 'q'):
        return
    elif(question == ''):
        print("Input required\n")
    else:
        if(sanitize):
            question = sani(question)
        if(check):
            check_sani_q(question)
        gem(question)