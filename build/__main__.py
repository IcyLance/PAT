from .funcmodule import gem_f, sani, check_sani_q, gpt_3, gpt_4, gem_p
from typing_extensions import Annotated
from typing import Optional
import typer
import os
import sys
from stat import S_ISFIFO
import tty
import termios

app = typer.Typer()

@app.callback()
def callback():
    """
    Choose an AI model you want to use. ***Be sure you have obtained the corresponding API key***.
    Can use the pipe operator to provide a question to PAT. 
    echo "Hello" | pat geminif
    """

@app.command()
def geminiP(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

    """
    Gemini-1.5-pro.
    """
    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    elif question == None: 
        print("Please input a question\n")
        return
 
    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    gem_p(question)

@app.command()
def geminiF(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="Cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

    """
    Gemini-1.5-flash.
    """
    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    elif question == None: 
        print("Please input a question\n")
        return
 
    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    gem_f(question)

@app.command()
def gpt3(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

    """
    Gpt-3.5-turbo ***UNTESTED*** 
    """
    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    elif question == None: 
        print("Please input a question\n")
        return
 
    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    gpt_3(question)

@app.command()
def gpt4(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize")
    ):

    """
    Gpt-4o-mini ***UNTESTED***
    """

    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    elif question == None: 
        print("Please input a question\n")
        return
 
    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    gpt_4(question)