# test
print "hello"
"""
You are given three integers x, y and z
representing the dimensions of a cuboid along with an integer n.
You have to print a list of all possible coordinates
given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
"""
x, y, z, n = (int(raw_input("Enter 4 integers: ")) for _ in range(4))
print [[a, b, c] for a in range(0, x+1) for b in range(0, y+1)
       for c in range(0, z+1) if a + b + c != n]
