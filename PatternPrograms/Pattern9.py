for i in range(1, 6): #rows
    for j in range(1, i+1):   #columns
        print("*", end=" ")
    print()
for i in range(5, 0, -1):
    for k in range(0, i-1):
        print("*", end=" ")
    print()