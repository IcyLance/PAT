from .funcmodule import gemini, sanitize

def main():
    raw_q = ''
    sani_q = ''
    while(raw_q != 'q'):
        raw_q = input('Input: ').strip()
        if(raw_q == 'q'):
            return
        elif(raw_q == ''):
            print("Input required\n")
        else:
            sani_q = sanitize(raw_q)
            gemini(sani_q)