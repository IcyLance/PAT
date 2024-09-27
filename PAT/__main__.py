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
    Can use the pipe operator to give PAT a file as a question. **Currently --check doesn't work with piping**.
    """

@app.command()
def geminiP(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(False, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

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
def geminiF(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="Cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(False, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

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
def gpt3(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(False, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

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
def gpt4(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(False, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

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