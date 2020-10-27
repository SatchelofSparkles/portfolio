#case insensitive
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def palindrome():
  word = input("what word do you want to check for palidromicity?\n")

  if is_palindrome(word):
    print('Yes! for', word, 'is totes the same as NOT_ALLOWED_ANYMORE')
  else:
    drow = word.lower()[::-1]
    print(f'Nay, for {word} is not the same as {drow}')

def main():
  palindrome()

main()