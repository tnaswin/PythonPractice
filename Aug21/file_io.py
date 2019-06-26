with open('app.log', 'w') as f:
   #first line
   f.write('my first file\n')
   #second line
   f.write('This file\n')
   #third line
   f.write('contains three lines\n')

with open('app.log', 'r') as f:
   content = f.readlines()

for line in content:
   print line

#Read From A File In Python
print "Read From A File In Python"
with open('app.log', 'w') as f:
   #first line
   f.write('my first file\n')
   #second line
   f.write('This file\n')
   #third line
   f.write('contains three lines\n')

f = open('app.log', 'r')
print f.read(10)    # read the first 10 data
#'my first f'

print f.read(4)    # read the next 4 data
#'ile\n'

print f.read()     # read in the rest till end of file
#'This file\ncontains three lines\n'

print f.read()  # further reading returns empty sting
#''
