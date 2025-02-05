from .funcmodule import gem_f, sani, check_sani_q, gpt_3, gpt_4, gem_p
from typing_extensions import Annotated
from typing import Optional
import typer
import os
import sys
from stat import S_ISFIFO

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
    question: Annotated[str, typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize"),
    f: bool = typer.Option(False, help="Writes the answer or output to a file called answer.txt")
    ):

    """
    Gemini-1.5-pro.
    """
    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    
    if question == None: 
        print("\n [-] Please input a question\n")
        return
 
    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    answer = gem_p(question)
    if f:
        try:
            with open('answer.txt', 'w') as out_file:
                out_file.write(answer)
        except Exception as e:
            print(f"Error when attempting to write answer to file: ", e)
    else:
        print("\n", answer, "\n")

@app.command()
def geminiF(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="Cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize"),
    f: bool = typer.Option(False, help="Writes the answer or output to a file called answer.txt")
    ):

    """
    Gemini-1.5-flash.
    """
    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
    
    if question == None: 
        print("\n [-] Please input a question\n")
        return
 
    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    answer = gem_f(question)
    if f:
        try:
            with open('answer.txt', 'w') as out_file:
                out_file.write(answer)
        except Exception as e:
            print(f"Error when attempting to write answer to file: ", e)
    else:
        print("\n\n", answer, "\n")


@app.command()
def gpt3(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize"),
    f: bool = typer.Option(False, help="Writes the answer or output to a file called answer.txt")
    ):

    """
    Gpt-3.5-turbo ***UNTESTED*** 
    """
    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return
        
    if question == None: 
        print("\n [-] Please input a question\n")
        return
 
    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    answer = gpt_3(question)
    if f:
        try:
            with open('answer.txt', 'w') as out_file:
                out_file.write(answer)
        except Exception as e:
            print(f"Error when attempting to write answer to file: ", e)
    else:
        print("\n\n", answer, "\n")

@app.command()
def gpt4(
    question: Annotated[Optional[str], typer.Argument(help="Input to the AI")] = None, 
    sanitize: bool = typer.Option(True, help="cleans input of sensitive info such as company names, phone numbers, and emails"), 
    check: bool = typer.Option(True, help="Prompts you with the sanitized input before sending. Can specifiy more info to sanitize"),
    f: bool = typer.Option(False, help="Writes the answer or output to a file called answer.txt")
    ):

    """
    Gpt-4o-mini ***UNTESTED***
    """

    piping = S_ISFIFO(os.fstat(0).st_mode)
    if piping:
        question = sys.stdin.read().strip()

    if question == 'q':
        return

    if question == None: 
        print("\n [-] Please input a question\n")
        return

    if sanitize:
        question = sani(question)

    if check:
        if piping:
            sys.stdin = open('/dev/tty', 'r')
            check_sani_q(question)
        else:
            check_sani_q(question)
    
    answer = gpt_4(question)
    if f:
        try:
            with open('answer.txt', 'w') as out_file:
                out_file.write(answer)
        except Exception as e:
            print(f"Error when attempting to write answer to file: ", e)
    else:
        print("\n\n", answer, "\n")