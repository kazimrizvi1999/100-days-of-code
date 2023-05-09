#Fabonacci series in which each number is the sum of two preceding numbers.
#like 0 1 1 2 3 5 8 13
#lets code
n1=0
n2=1
num=int(input('Enter the range of Fabonacci series'))
print(n1)
print(n2)
for i in range(2,num+1):
    sum = n1 + n2
    n1=n2
    n2=sum
    print(n2)



