#maximum no of list
l=[2,34,100,23,33,9]
max=l[0]
for i in range(len(l)):
    if l[i] >max:
        max=l[i]
print(max)