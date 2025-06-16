import re

def edited_num(Phone_number):
    clean_num = re.sub(r'[^\d+]',  '',Phone_number)
    if clean_num.startswith('+'):
        return print(clean_num)
    elif clean_num.startswith('38') and not clean_num.startswith('+380'):
        return print("+380" + clean_num[3:])
    elif clean_num.startswith('380'):
        return print("+" + clean_num)
    else:
        return print('+38' + clean_num)
    
edited_num('3516100203')
