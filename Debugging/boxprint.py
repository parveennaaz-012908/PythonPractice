'''
a boxPrint() function that takes a character, a width, and a height, and uses the character to make a little picture of a box with that width and height. 
This box shape is printed to the screen.
hi
'''


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
      raise Exception('Symbol must be a single character string.')
    if width <= 2:
      raise Exception('Width must be greater than 2.')
    if height <= 2:
      raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

if __name__=='__main__':

    # TO run successfully change the 3 filed width value and 4th zz to one character
    for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
       try:
         boxPrint(sym, w, h)
       except Exception as err:
            print('An exception happened: ' + str(err))