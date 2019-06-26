def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print "%d squared is %d." % (n, squared)
    print type (squared)
    return squared

# Call the square function.

square(10)


def power(base, exponent):
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)

import math

print "Square root of 25: " + str(math.sqrt(25))
