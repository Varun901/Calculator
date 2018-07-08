# File: CCC_2018_JuniorContest1
# Junior 1 - Telemarketer or not?
# A system to determine whether a number is from a telemarketer
number = [int(input()) for i in range(4)]

if number[0] == 8 or number[0] == 9:
  if number[1] == number[2]:
    if number[3] == 8 or number[3] == 9:
      print ("ignore")
    else:
      print ("answer")
  else:
    print ("answer")
else:
  print ("answer")