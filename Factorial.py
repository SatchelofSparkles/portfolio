def Factorial():
  num = int(input('enter the number you wish to find the factorial of'))
  fact = int(1)
  while num >= 1:
    fact = fact * num
    num = num - 1
  print(fact)
Factorial()