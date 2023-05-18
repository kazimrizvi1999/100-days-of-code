arr=[1,2,4,2,1,1,13,3]
count=0
num=int(input('Select any num from array: '))
for i in arr:
    if i == num:
        count+=1
print(count)