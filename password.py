import random

def password_generator():

    uppercase_letter1 = chr(random.randint(65, 90))
    uppercase_letter2 = chr(random.randint(65, 90))

    lowercase_letter1 = chr(random.randint(97, 122))
    lowercase_letter2 = chr(random.randint(97, 122))

    digit1 = chr(random.randint(48, 57))
    digit2 = chr(random.randint(48, 57))

    punctuation_sign1 = chr(random.randint(33, 152))
    punctuation_sign2 = chr(random.randint(33, 152))

    password = uppercase_letter1 + uppercase_letter2 + lowercase_letter1 \
               + lowercase_letter2 + digit1 + digit2 +\
               punctuation_sign1 + punctuation_sign2

    random.shuffle(list(password))

    return print(password)


password_generator()
