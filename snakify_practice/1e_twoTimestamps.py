# This program finds the difference between two timestamps given in hour, minute, and second format.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
print((3600 * (d-a)) + (60 * (e - b)) + (f - c))