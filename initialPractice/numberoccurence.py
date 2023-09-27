
numberlist=[23,6,3,5,6,8,9,2,1,3,5,13,5,3,6,7,89,0,135,77,134,5,6,67,8,9,9]
print(numberlist)
num_occurence={}
for i in numberlist:
  if i in num_occurence:
    num_occurence[i]+=1
  else:
    num_occurence[i]=1
print(num_occurence)