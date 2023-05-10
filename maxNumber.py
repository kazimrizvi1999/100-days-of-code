arr=[1,2,34,6,78]

max=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)