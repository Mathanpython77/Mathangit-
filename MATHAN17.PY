#min no of a list
l=[2,34,100,23,33,9]
min =l[0]
for i in range (len(l)):
    if l[i]<min:
        min=l[i]
print(min)