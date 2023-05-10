array=[]

n=int(input('Enter how many numbers you want to add in array'))
for i in range(0,n):
   element=int(input('Enter any number'))
   array.append(element)
print(array) 
sum=0
for i in array:
   sum= sum + i
print(sum)

   