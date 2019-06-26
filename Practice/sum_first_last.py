def sum_of_digits(n):
    f = n % 10
    while n > 10:
        n = n // 10
    return (f + n)


n = []
for i in range(int(input("Enter the number of test cases: "))):
    n.append(int(input()))
print("Sum of first and last digits: ")
for i in range(len(n)):
    print(sum_of_digits(n[i]))
