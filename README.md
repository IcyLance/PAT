# PAT - Pentester Assistant

## Description
Tool for discrete CLI AI usage. Built for pentesters.

Clears your question of most company names, phone numbers, and emails.

Currently only supports gemini 1.5 flash and pro, gpt 3.5 turbo and 4.

## API keys
Before using PAT you will need to get an API key from your prefered AI model.

Go [here](https://aistudio.google.com/app/apikey) to get an API key for the Gemini models.

Go [here](https://platform.openai.com/api-keys) for gpt API key. Beware this will require an account and payment.

**--NOTICE: GPT models havent been fully tested.--**

Once you have your API key(s) find the build folder.
``` bash
cd build
```
Then in sample.env replace "YOUR_API_KEY" with your API key.


## Install and run
You should start a virtual environment as pip causes trouble otherwise.

Install the virtual environment app.
```bash
sudo apt-get install python3-venv
```

Create the environment.
```bash
python3 -m venv env #(env is the name. can change at will)
```

Run the environment.
```bash
source env/bin/activate
```

Make sure you are in the PAT directory, then install.
```bash
pip3 install -e .
```
Finally run pat
```bash
pat
```