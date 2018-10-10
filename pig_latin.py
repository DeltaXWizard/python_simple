pig = 'ay'
none = "empty"

original = raw_input('Enter a word:') # not sure which version this supports in Python, should be updated to 3.x

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pig
  new_word = new_word[1:len(new_word)]
  print (new_word)
else:
    print (none)
