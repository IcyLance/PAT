from .funcmodule import gem_f, sani, check_sani_q, gpt_3, gpt_4, gem_p
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
def geminiP(question: Annotated[Optional[str], typer.Argument()] = None, sanitize: bool = True, check: bool = False):
    """
    Gemini-1.5-pro.
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
        gem_p(question)

@app.command()
def geminiF(question: Annotated[Optional[str], typer.Argument()] = None, sanitize: bool = True, check: bool = False):
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
        gem_f(question)

@app.command()
def gpt3(question: Annotated[Optional[str], typer.Argument()] = None, sanitize: bool = True, check: bool = False):
    """
    Gpt-3.5-turbo ***UNTESTED***
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
        gpt_3(question)

@app.command()
def gpt4(question: Annotated[Optional[str], typer.Argument()] = None, sanitize: bool = True, check: bool = False):
    """
    Gpt-4o-mini ***UNTESTED***
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
        gpt_4(question)