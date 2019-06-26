#check if integer
num = int(raw_input("Enter a number: "))


def is_int(x):
    if x % 1 == 0:
        print "Integer"
        return True
    else:
        print "Not an Integer"
        return False

#digit sum
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
    print "Sum of digits: " + str(total)
    return total

#factorial
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    print "Factorial: " + str(total)
    return total

#check prime
def is_prime(x):
    if x < 2:
        print "Not a Prime number"
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                print "Not a Prime Number"
                return False
        print "Prime Number"
        return True

is_int(num)
digit_sum(num)
factorial(num)
is_prime(num)
