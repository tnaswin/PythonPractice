#Fibonacci: 0 1 1 2 3 5 8 13 21
import timeit

def fibo(x):
    a = int(0)
    b = int(1)
    print a
    print b
    for i in range(x-2):
        temp = b
        b = a + b
        a = temp
        print b

print timeit.default_timer()
fibo(x = int(raw_input("Enter a number: ")))
print timeit.timeit()
