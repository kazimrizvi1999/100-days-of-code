num=int(input('Enter any number'))
count=0
if num == 1:
    print('It is not a Prime number')
else:
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
    if count ==  2:
        print('It is a Prime number')
    else:
        print('not a prime number')

