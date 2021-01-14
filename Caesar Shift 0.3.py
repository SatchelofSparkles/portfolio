def caesar(string, n):
  Shift1 = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'a', ' ':' ', ',':',', '"':'"', "'":"'", ".":".", ";":";", ":":":", "(":"(", ")":")", "!":"!", "?": "?", "/":"/", "-":"-", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "0":"0"}
  
  string_as_list = list(string)
  new_list = []
  n = n%25
  i = 0
  while i < n:
    i += 1
    new_list = []
    for char in string_as_list:
      new_list.append(Shift1.get(char))
      string_as_list = new_list

  
  print(''.join(string_as_list))


caesar("yes, um... it's five fifteen", 3)

def decode_caesar(string):
  Shift1 = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'a', ' ':' ', ',':',', '"':'"', "'":"'", ".":".", ";":";", ":":":", "(":"(", ")":")", "!":"!", "?": "?", "/":"/", "-":"-", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "0":"0"}
  
  string_as_list = list(string)
  new_list = []
  i = 0
  while i < 25:
    i += 1
    new_list = []
    for char in string_as_list:
      new_list.append(Shift1.get(char))
      string_as_list = new_list
    print((26-i), ''.join(new_list))

decode_caesar("bhv, xp... lw'v ilyh iliwhhq")