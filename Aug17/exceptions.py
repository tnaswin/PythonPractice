# Python program to handle simple runtime error

a = [1, 2, 3]
try:
    print "Second element = %d" %(a[1])

    # Throws error since there are only 3 elements in array
    print "Fourth element = %d" %(a[3])

except IndexError:
    print "An error occurred"

# Program to handle multiple errors with one except statement
try :
    a = 3
    if a < 4 :
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
     
    # throws NameError if a >= 4
    print "Value of b = ", b

except(ZeroDivisionError, NameError):
    print "\nError Occurred and Handled"
