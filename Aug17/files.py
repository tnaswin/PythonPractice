my_list = [i ** 2 for i in range(1, 11)]

my_file = open("text.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

###

my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

with open("text.txt", "w") as my_file:
    my_file.write("My Data!")

if not file.closed:
    file.close()

print my_file.closed
