l = []
n = int(input("Enter the number: "))
m = int(input("Enter the size: "))
for i in range(n):
    l.append([])

    for j in range(m):
        x = input("Enter the element: ")
        l[i].append(x)
print(l)

