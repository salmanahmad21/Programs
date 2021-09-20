# Write a Python program to print all natural numbers in reverse (from 10 to 1).
for i in range(10, 0, -1):
    print(i)


# Write a Python program to print all even numbers between 1 to 100.
for i in range(1, 101):
    if (i % 2) == 0:
        print(i)

# Write a Python program to print all odd numbers between 1 to 100.
for i in range(0, 100):
    if (i % 2) == 1:
        print(i)

# Write a Python program to find sum of all natural numbers between 1 to 10.
sum = 0
for i in range(1, 11):
    sum = sum+i
print(sum)


# Write a Python program to find sum of all even numbers between 1 to 10.
sum = 0
for i in range(1, 11):
    if (i % 2) == 0:
        sum = sum+i
print(sum)


# Write a Python program to find sum of all odd numbers between 1 to 10.
sum = 0
for i in range(1, 10):
    if (i % 2) == 1:
        sum = sum+i
print(sum)


# Write a Python program to print multiplication table of any number.
print("please enter a number.")
n = int(input())
m = 1
for i in range(1, 11):
    m = n*i
    print(n, "X", i, "=", m)
