def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * (factorial(n - 1))

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

n = int(raw_input("Enter a number: "))
if n <= 0:
    print("Plese enter a positive integer")
else:
    print "Factorial: ", factorial(n)
    print "Fibonacci: ",
    for i in range(n):
        print(fibonacci(i)),
