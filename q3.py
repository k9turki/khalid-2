arr1=[0,1]
for i in range (2,10):
    arr1.append(arr1[i-1]+arr1[i-2])
    # arr1.append(arr1[2])
print(arr1)

