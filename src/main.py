# Resolve the problem!!
import string
import random
SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    len_password= random.randrange(8,16)
    password_generated = []
    i=0
    while i < len_password:
        lower_letter = chr(random.randrange(97,122))
        upper_letter = chr(random.randrange(65,90))
        number_str = str(random.randrange(0,9))
        lent_symbol = len(SYMBOLS)
        random_simbol = random.randrange(0,lent_symbol)
        slect_symbol = SYMBOLS[random_simbol]
        if i == 0:
            password_generated.append(lower_letter)
            password_generated.append(upper_letter)
            password_generated.append(number_str)
            password_generated.append(slect_symbol)
            i +=4
        else:
            x = random.randrange(1,4)
            if x == 1:
                password_generated.append(lower_letter)
                i +=1
            elif x == 2:
                password_generated.append(upper_letter)
                i +=1
            elif x == 3:
                password_generated.append(number_str)
                i +=1
            elif x == 4:
                password_generated.append(slect_symbol)
                i +=1
    Str_passwaord =''.join(password_generated)
    print(f'Password generado = {Str_passwaord}')
    return Str_passwaord


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
