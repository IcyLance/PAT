from .funcmodule import gem, sani, check_sani_q, gpt
from typing_extensions import Annotated
from typing import Optional
import typer
import select
import sys

app = typer.Typer()

@app.callback()
def callback():
    """
    Choose an AI model you want to use. ***Please be sure you have obtained the corresponding API key***.
    """

@app.command()
def gemini(question: Annotated[Optional[str], typer.Argument()] = None, sanitize: bool = True, check: bool = False):
    """
    Gemini-1.5-flash.
    """
    if select.select([sys.stdin], [], [], 0)[0]:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    elif question == None: 
        print("Please input a question\n")
    else:
        if sanitize:
            question = sani(question)
        if check:
            check_sani_q(question)
        gem(question)

@app.command()
def gpt(question: Annotated[Optional[str], typer.Argument()] = None, sanitize: bool = True, check: bool = False):
    """
    Gpt-3.5-turbo
    """
    if select.select([sys.stdin], [], [], 0)[0]:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    elif question == None: 
        print("Please input a question\n")
    else:
        if sanitize:
            question = sani(question)
        if check:
            check_sani_q(question)
        gem(question)