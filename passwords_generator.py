from random import choice

def count():
    n = input('Количество генерируемых паролей? Укажи цифру: ')
    while n.isdigit() == False:
        print('Нужно вводить цифу, попробуй еще раз!')
        n = input('Сколько нужно паролей? Укажи цифру: ')
    return int(n)

def long():
    l = input('Требуемая длина пароля: ')
    while l.isdigit() == False:
        print('Нужно вводить цифу, попробуй еще раз!')
        l = input('Требуемая длина пароля: ')
    return int(l)

def is_number():
    isn = input('Нужны ли в пароле цифры 0123456789? (y/n): ')
    while isn.lower() not in ['y', 'n']:
        print('Нужно вводить "y" или "n".')
        isn = input('Нужны ли в пароле цифры 0123456789? (y/n): ')
    return isn

def is_upper():
    isup = input('Нужны ли в пароле заглавные буквы? (y/n): ')
    while isup.lower() not in ['y', 'n']:
        print('Нужно вводить "y" или "n".')
        isup = input('Нужны ли в пароле заглавные буквы? (y/n): ')
    return isup

def is_lower():
    islw = input('Нужны ли в пароле строчные буквы? (y/n): ')
    while islw.lower() not in ['y', 'n']:
        print('Нужно вводить "y" или "n".')
        islw = input('Нужны ли в пароле строчные буквы? (y/n): ')
    return islw
    
def is_symbol():
    issmb = input('Нужны ли в пароле символы? (y/n): ')
    while issmb.lower() not in ['y', 'n']:
        print('Нужно вводить "y" или "n".')
        issmb = input('Нужны ли в пароле символы? (y/n): ')
    return issmb

def is_ambiguous():
    amb = input('Будут ли в пароле неоднозначные символы "il1Lo0O"? (y/n): ')
    while amb.lower() not in ['y', 'n']:
        print('Нужно вводить "y" или "n".')
        amb = input('Могут ли быть в пароле неоднозначные символы "il1Lo0O"? (y/n): ')
    return amb

def gen_chars():
    chars = ''
    if isn == 'y':
        chars += '0123456789'
    if isup == 'y':
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if islw == 'y':
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if issmb == 'y':
        chars += '!#$%&*+-=?@^_'
    if amb == 'n':
        for i in range(len(chars)):
            if chars[i] in 'il1Lo0O':
                del chars[i]
    return chars

def build_password():
    for i in range(n):
        password = []
        for i in range(l):
            password.append(choice(chars))
        print(''.join(password))
        
n = count()
l = long()
isn = is_number()            
isup = is_upper()
islw = is_lower()
issmb = is_symbol()
amb = is_ambiguous()
chars = gen_chars()
build_password()