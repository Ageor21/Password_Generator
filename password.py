import random

# This function generates a random password
def password_generator():

    # Generates 2 random capital letters using the ASCII code 
    uppercase_letter1 = chr(random.randint(65, 90))
    uppercase_letter2 = chr(random.randint(65, 90))
    
    # Generates 2 random lowercase letters using the ASCII code 
    lowercase_letter1 = chr(random.randint(97, 122))
    lowercase_letter2 = chr(random.randint(97, 122))
    
    # Generates 2 random numbers using the ASCII code 
    digit1 = chr(random.randint(48, 57))
    digit2 = chr(random.randint(48, 57))
    
    # Generates 2 random symbols using the ASCII code 
    punctuation_sign1 = chr(random.randint(33, 152))
    punctuation_sign2 = chr(random.randint(33, 152))
    
    # Combines all variables into one 
    password = uppercase_letter1 + uppercase_letter2 + lowercase_letter1 \
               + lowercase_letter2 + digit1 + digit2 \
               + punctuation_sign1 + punctuation_sign2

    # Shuffles all characters around
    random.shuffle(list(password))
    
    # Returns the output 
    return print(password)


# Prints fucntion 
password_generator()
