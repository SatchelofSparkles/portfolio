#successful Fibonacci value
def Fibonacci():
  Fib = [0, 1]
  count = 1
  a = 0
  b = 1
  while count <= 50:
    count = count + 1
    a, b = b, a+b
    Fib.append(b)
  index = input('Which Fibonacci number do you want to know? ')
  print('The', index, 'th Fibonacci number is', Fib[int(index)])
Fibonacci()