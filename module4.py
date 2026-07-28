N = int(input("Enter N: "))

numbers = []

for i in range(N):
    num = int(input("Enter a number: "))
    numbers.append(num)

X = int(input("Enter X: "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)