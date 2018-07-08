# File: CCC_2018_JuniorContest3
# Junior 3 - Are we there yet?
# A system to determine distance between cities
d = list(map(int, input().split()))

print("0", d[0], d[0] + d[1], d[0] + d[1] + d[2], d[0] + d[1] + d[2] + d[3])
print(d[0], "0", d[1],  d[1] + d[2], d[1] + d[2] + d[3])
print(d[0] + d[1], d[1], "0", d[2], d[2] + d[3])
print(d[0] + d[1] + d[2], d[1] + d[2], d[2], "0", d[3])
print(d[0] + d[1] + d[2] + d[3], d[1] + d[2] + d[3], d[2] + d[3], d[3], "0")