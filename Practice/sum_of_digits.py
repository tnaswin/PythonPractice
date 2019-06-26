def sum_of_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

n = []
for i in range(int(input("Enter the number of test cases: "))):
    n.append(int(input()))
print("Sum of digits: ")
for i in range(len(n)):
    print(sum_of_digits(n[i]))
