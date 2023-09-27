import pyinputplus as pyip

def addsUptoTen(numbers):
    numbersList=list(numbers)
    for i, digit in enumerate(numbersList):
        print(i)
        numbersList[i]=int(digit)
    if sum(numbersList)!=10:
            raise Exception ('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers)

if __name__=='__main__':
    #response= pyip.inputNum()
    #response = pyip.inputInt(prompt='Enter a number: ')
    #response1=input('Enter the number:')
    #response=pyip.inputInt('Enter the Integer value:' , min=2)
    #response1=pyip.inputInt('Enter the Integer value:', max=5)
    #response3=pyip.inputInt('Enter the Integer value:', greaterThan=4)
    #response4=pyip.inputInt('Enter the Integer Value:', lessThan=10)
    #response5=pyip.inputNum('Enter the Blank Value: ',blank=True)
    #response6=pyip.inputNum('Enter the Num:',limit=2)
    #response6=pyip.inputNum('Enter the Num:',timeout=2)
    #response7=pyip.inputNum('Enter the num:',limit=2,default='N/A')
    #response=pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) # accept the roman letter, even though is invalid.
    #response=pyip.inputNum(blockRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
    #response=pyip.inputNum(blockRegexes=[r'[02468]$'])
    #response=pyip.inputStr(allowRegexes=[r'Vasant','Prashant'],blockRegexes=[r'cat'])
    #response=pyip.inputCustom(addsUptoTen)
    while True:
        prompt = 'Want to know how to keep an idiot busy for hours?\n'
        response=pyip.inputYesNo(prompt)
        if response=='no':
             break
        
        print(response)
    print('Thank you. Have a nice day.')
    while True:
         prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
         response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
         if response == 'no':
              break
    print('Gracias. Que tenga un lindo día')
              