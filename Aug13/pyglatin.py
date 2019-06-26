# Move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay."


pyg = 'ay'

original = raw_input("Enter a word:")

if len(original) > 0 and original.isalpha():
    word = original.lower()
    print word
    first = word[0]
    new_word = word + first + pyg
    print new_word
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'
