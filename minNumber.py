arr=[1,5,0,4,6,45]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]< min:
        min=arr[i]
print(min)