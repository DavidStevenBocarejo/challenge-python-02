#Generar letras al azar
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def generar_letras():
    len_password= random.randrange(8,16)
    assci_lower_letter = random.randrange(97,122)
    assci_upper_letter = random.randrange(65,90)
    number = random.randrange(0,9)
    print(f'Lent password= {len_password}')
    print(f'Codigo assci lower {assci_lower_letter} = {chr(assci_lower_letter)}')
    print(f'Codigo assci Uper {assci_upper_letter} = {chr(assci_upper_letter)}')
    print(f'Numero = {number}')

    lent_symbol = len(SYMBOLS)
    random_simbol = random.randrange(0,lent_symbol)
    slect_symbol = SYMBOLS[random_simbol]
    print(f'Indice del simbolo = {random_simbol} --- Simbolo seleccionado = {slect_symbol}')
    #letter = 'A' 
    #assci = ord(letter)
    #assci = 65
    #letter = chr(assci)
    #print(f'El valor de {assci} es {letter}')
    password_generated = []
    i=0
    while i < len_password:
        print(f'I en ciclo = {i}')
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


    print(password_generated)
    print(f'Longitud de la contraseña= {len(password_generated)}')
    Str_passwaord =''.join(password_generated)
    print(f'STRING = {Str_passwaord}')





if __name__ == "__main__":
    generar_letras()
