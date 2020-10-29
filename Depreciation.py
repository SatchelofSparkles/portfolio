#Motorbike value tracker
m = 2000
count = 0
print("year", count, "£", m)
while m >= 1000:
  count = count + 1
  m = m*.9
  print("year", count, "£", round(m, 2))
#note: gives some values as eg £1620.0 which is incorrect formatting

#hacky solution:
m = 2000
count = 0
print("year", count, "£", m)
while m >= 1000:
  count = count + 1
  m = m*.9
  print("year", count, "£", int((m//1)), ".", int(round(m%100, 0)))
  #better, still far from perfect