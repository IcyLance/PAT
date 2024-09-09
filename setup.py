from setuptools import setup

setup(
    name='pat',
    version='0.0.1',
    author='William Oldert',
    descritption="Tool for discrete CLI AI usage. Built for pentesters.",
    license='LICENSE',
    packages=['PAT'],
    install_requires=[
        'python-dotenv <= 1.0.0',
        'google-generativeai',
    ],
    entry_points={
        'console_scripts': [
            'pat = PAT.__main__:main'
        ]
    }
)