#count of repeating items
def count(sequence, item):
    print sequence, item
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    print "No. of occurence: ",
    return count

#remove odd numbers from the list
def purify(lst):
    print lst
    res = []
    for i in lst:
        if i % 2 == 0:
            res.append(i)
    print "Filtered List: ",
    return res

#product
def product(list):
  print list
  total = 1
  for num in list:
    total = total * num
  print "Product: ",
  return total

#remove duplicates
def remove_duplicates(inputlist):
    print inputlist
    if inputlist == []:
        return []

# Sort the input list from low to high
    inputlist = sorted(inputlist)
# Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
    print "Duplicates Removed: "
    return outputlist

print count([1, 2, 1, 1], 1)
print purify([1,2,3,4,5,6,7,8,9])
print product([5,4,4])
print remove_duplicates([1,2,2,4,3,5,3,6,2,7,8,9])
