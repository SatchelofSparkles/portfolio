#case sensitive
def palindrome():
  word = input("what word do you want to check for palidromicity?\n")
  drow = word[::-1]
  if word == drow:
    print('Yes! for', word, 'is totes the same as ', drow)
  else:
    print('Nay, for', word, 'is not the same as ', drow)
palindrome()