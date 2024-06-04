def collatz(number):
  if number % 2==0:
    number=(number // 2)
    print(number)
    return(number)
  elif number % 2 == 1:
    number=(3 * number + 1)
    print(number)
    return(number)

try:
  num=input()
  while num!=1:
    num=collatz(int(num))
except:
  print('Enter integer number')
