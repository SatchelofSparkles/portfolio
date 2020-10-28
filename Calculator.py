def calculator():
  val1 = input('first value pls \n')
  val2 = input('and the second \n')
  operator = input('do you want to \n a) add \n b) subtract \n c) multiply \n d) divide \n e) raise to the power of \n f) square \n')
  if operator == 'a':
    val3 = float(val1) + float(val2)
    print(val1 ,'+' ,val2 ,'=' , val3)
  elif operator == 'b':
    val3 = float(val1) - float(val2)
    print(val1, '-' ,val2 ,'=' ,val3)
  elif operator == 'c':
    val3 = float(val1) * float(val2)
    print(val1, 'x' ,val2 ,'=' ,val3)
  elif operator == 'd':
    val3 = float(val1) / float(val2)
    print(val1, '/' ,val2 ,'=' ,val3)
  elif operator == 'e':
    val3 = float(val1) ** float(val2)
    print(val1, '^' ,val2 ,'=' ,val3)
  elif operator == 'f':
    val3 = float(val1)**2
    val4 = float(val2)**2
    print('well, I can\'t exactly do \"', val1, 'square' ,val2 ,'\", but ' ,val1, 'squared is ',val3, ", and ", val2, "squared is " , val4 )
  else:
    print('wait, you want to what now? that wasn\'t an option. Go away, silly person!')
calculator()