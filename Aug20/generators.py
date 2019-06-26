def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1

for i in counter_generator(5,10):
    print i,
print

###
def infinite_generator(start=0):
    while True:
        yield start
        start += 1

for num in infinite_generator(4):
    print num,
    if num > 20:
        break
print
