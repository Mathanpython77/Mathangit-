start = 4
end = 4

for i in range(9):
    for j in range(10):
        if j >= start and j <= end:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(' ')
    if i<4-1:
        start-=1
        end+=1
    else:
        start+=1
        end-=1
