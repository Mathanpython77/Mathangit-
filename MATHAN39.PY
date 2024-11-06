#pattern design
start=4
end=4
for i in range(5):
    for j in range(5):
        if j >= start:
            print(" * ",end=" ") 
        else:
            print(" ",end=" ")
    print(' ')
    start-=1