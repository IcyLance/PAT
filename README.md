# PAT - Pentester Assistant

## Description
Tool for discrete CLI AI usage. Built for pentesters.

Clears your question of most company names, phone numbers, emails, IPv4 an IPv6 addresses.

Currently only supports gemini 1.5 flash and pro, gpt 3.5 turbo and 4.

#### Additionally
If you notice a company name that you have to specify for redaction please either open an issue or add it to list.txt and submit a pull request.
Same for if you notice any other issues or errors!

## API keys
Before using PAT you will need to get an API key from your prefered AI model.

Go [here](https://aistudio.google.com/app/apikey) to get an API key for the Gemini models.

Go [here](https://platform.openai.com/api-keys) for gpt API key. Beware this will require an account and payment.

**--NOTICE: GPT models havent been fully tested.--**

Once you have your API key(s) find the build folder.
``` bash
cd build
```
Then inside the build directory, create a .env file.
Be sure that the file is simply ".env" as only then will the program work.
Please be careful of pushing any changes with you API key in it.
``` bash
mkdir .env
```
Copy sample.env into your new .env file, replacing "YOUR_API_KEY" with your API key.


## Install and run
You should start a virtual environment as pip causes trouble otherwise.

Install the virtual environment app.
```bash
sudo apt-get install python3-venv
```

Create the environment.
The 2nd venv is the name. You can change its name at will.
```bash
python3 -m venv venv 
```

Run the environment.
Be sure you replace venv with whatever you named your venv file, if you changed it.
```bash
source venv/bin/activate
```

Make sure you are in the PAT directory, then install.
```bash
pip3 install -e .
```
Finally run pat
```bash
pat
```

Additional features to add:
Implement more error checking.
Make converstions possible?
Add locations to sanitizer?
Only replace company name if capitalized?