# File: CCC_2018_JuniorContest2
# Junior 2 - Occupy Parking
# A system to determine parking availability

n = int(input())
a = str(input())
b = str(input())
x = 0
y = 0


for i in range(n):
  if a[y] == "C" and b[y] == "C":
    x = x + 1
  elif a[y] == "." or b[y] == ".":
    x = x + 0
  y = y + 1

print (x)