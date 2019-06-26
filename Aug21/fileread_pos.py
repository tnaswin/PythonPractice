with open('app.log', 'w') as f:
   #first line
   f.write('It is my first file\n')
   #second line
   f.write('This file\n')
   #third line
   f.write('contains three lines\n')

#Open a file
f = open('app.log', 'r+')
data = f.read(19);
print 'Read String is : ', data

#Check current position
position = f.tell();
print 'Current file position : ', position

#Reposition pointer at the beginning once again
position = f.seek(0, 0);
data = f.read(19);
print 'Again read String is : ', data

#Close the opened file
f.close()

"""
import os

#Rename a file from <app.log> to <app1.log>
os.rename( "app.log", "app1.log" )

#Delete a file <app1.log>
os.remove( "app1.log" )
"""
