# CAPTCHA GENERATOR
# import random module
import random as rd
# function defining
def captcha_code():

    _upper1 = ord(rd.choice(chr(rd.randint(65,90))))
    _upper2 = ord(rd.choice(chr(rd.randint(65,90))))
    # print(_upper1,_upper2)

    _lower1=ord(rd.choice(chr(rd.randint(97,122))))
    _lower2=ord(rd.choice(chr(rd.randint(97,122))))
    # print(_lower1,_lower2)

    number1=rd.randint(0,9)
    number2=rd.randint(0,9)
    # print(number1,number2)

    _symbol1=ord(rd.choice(chr(rd.randint(33,38))))
    _symbol2=ord(rd.choice(chr(rd.randint(33,38))))
    # print(_symbol1,_symbol2)

    list=[chr(_upper1),chr(_upper2),chr(_lower1),chr(_lower2),number1,number2,chr(_symbol1),chr(_symbol2)]
    rd.shuffle(list)

    for i in list:
        print(i,end=' ')

# Function calling
captcha_code()


