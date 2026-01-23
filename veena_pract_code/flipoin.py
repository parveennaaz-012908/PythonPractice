import random
 
streak_length = 6
num_of_streak_count = 0

for experimentNumber in range(10000):
   
   flip_list = []
   a = 0
   for flips in range(100):
       flip = random.randint(0,1)
       if flip == 0:
         flip_list.append('T')
       else:
          flip_list.append('H')
   
         
   while a <= (len(flip_list) - streak_length):
        streak_ok = True
        for s in range(1, streak_length):
            if flip_list[a] != flip_list[a + s]:
                streak_ok = False
                break
 
        if streak_ok:
            num_of_streak_count += 1
            a += streak_length
        else:
            a += 1
   print('num_of_streak_count: ',num_of_streak_count)
     
     
     
""""
   while a <= (len(flip_list) - streak_length):
     #if (flip_list[a] == flip_list[b]):
        streak_ok = True
        for s in range(1,streak_length):
           if flip_list[a] != flip_list[a+s]:
              streak_ok = False
              break
 
        if streak_ok:
            num_of_streak_count += 1
            a = a + streak_length
            #   b = a+1
        else:
              a += 1
            #  b = a+1
    # else:
       #  a += 1
       #  b = a+1
"""  
#print(num_of_streak_count)
#print('Chance of streak: %s%%' % (num_of_streak_count / 100))
     