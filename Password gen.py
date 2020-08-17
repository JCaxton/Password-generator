#  First, Import the libraries to be used.

import random, math


#  Create a function which will generate a password.

def genpass():
    """This function generates a random password"""
    #  Create a string variable which stores all 'strings'.
    OTP = '@!_/#%*0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    password = ""
    length = len(OTP)
    for i in range(6):
        password += OTP[math.floor(random.random() * length)]

    return password


#  Driver code

if __name__ == "__main__":
    print("New Password of length 6:", genpass())
