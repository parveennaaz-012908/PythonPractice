import random
''' This function is used to generate number'''

def getRandomNum(num_digit):
    print(" Generate Secret Number")
    digit=list('0123456789')
    random.shuffle(digit)
    return "".join(digit[:num_digit])

