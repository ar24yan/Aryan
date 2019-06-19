l = []
N = int(input("Enter the number: "))
M = int(input("Enter the size: "))
for i in range(N):
    l.append([])

    for j in range(M):
        x = input("Enter the element: ")
        l[i].append(x)
print(l)

