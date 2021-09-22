a = [[1, 2, 3], [7, 8, 9]]
b = [[5, 6, 7], [3, 4, 5]]
c = []

for row in range(2):
    for col in range(3):
        c.append(a[row][col] + b[row][col])

print(c)
