l=[2,3,6,9]
even=[]
odd=[]
for i in range (0,4,1):
    y=l[i]
    if y % 2 ==0:
        even.append(y)
    else:
        odd.append(y)
print(even)
print(odd)
