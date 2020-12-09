#  First, Import the libraries to be used.

import random
import string


Letters = string.ascii_letters
Numbers = string.digits
Symbols = string.punctuation


def pass_combo_choice():
    '''Prompts user to choose password character combination which could either be digits, letters,
    punctuation or mix of either of them:
    returns list <class 'list'> of boolean. Defaults to [True, True, True] for invalid choices
    0th list item represents numbers
    1st list item represents letters
    2nd list item represents punctuation.'''
    # Get user's password combination choice.
    want_numbers = input("Any numbers? (True or False): ")
    want_letters = input("Any letters? (True or False): ")
    want_symbols = input("Any symbols? (True or False): ")

    # convert to answers boolean.
    try:
        want_numbers = eval(want_numbers.title())
        want_letters = eval(want_letters.title())
        want_symbols = eval(want_symbols.title())
        return [want_numbers, want_letters, want_symbols]

    except NameError as er:
        print("Please use either True Or False.")
        print("Invalidity returns default, regenerate again.")

    return [True, True, True]


def fetch_string_constant(choice_list):
    '''Returns a string constant based on users choice_list.
    Returned string constant can either be digits, letters, punctuation or
    combination of them:
    choice_list --> list <class 'list'> of boolean
    0th list item represents numbers
        True to add digits to constant False otherwise
    1st list item represents letters
        True to add letters to constant False otherwise
    2nd list item represents punctuation
        True to add punctuation to constant False otherwise'''
    string_constant = ''
    string_constant += Numbers if choice_list[0] else ''
    string_constant += Letters if choice_list[1] else ''
    string_constant += Symbols if choice_list[2] else ''
    return string_constant


# Specify length of the password.

def get_password_length():
    '''Retrieves length of the desired password; returns number <class int>'''
    length = input("Insert password length: ")
    return int(length)

#  Create a function which will generate a password.

def genpass(cbl, length=8):
    '''This function generates a random password. Defaults to 8 if nothing is specified:
    returns string <class str>'''
    # create alphanumerical from strings.
    printable = fetch_string_constant(cbl)

    # convert printable to list from string then shuffle.
    printable = list(printable)
    random.shuffle(printable)

    # generate password.
    new_password = random.choices(printable, k=length)
    new_password = ''.join(new_password)
    return new_password


# Driver code.
if __name__ == "__main__":
    length = get_password_length()
    choice_list = pass_combo_choice()
    password = genpass(choice_list, length)
    print("New password\n", password)



    #  Create a string variable which stores all 'strings'.
    #char = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    #length = len(char * 3)
    #password = ''.join(random.choice(char) for i in range(length)
    #print('New password is: ', password)

    #return password


#  Driver code

#if __name__ == "__main__":
    #print("New Password: ", genpass())
