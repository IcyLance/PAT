from setuptools import setup, find_packages

setup(
    name='pat',
    version='1.0.0',
    author='William Oldert',
    descritption="Tool for discrete CLI AI usage. Built for pentesters.",
    license='LICENSE',
    packages=find_packages(),
    install_requires=[
        'python-dotenv <= 1.0.0',
        'google-generativeai',
        'typer >= 0.12.5',
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'pat = build.__main__:app'
        ]
    }
)