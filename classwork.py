# n = int(input())
# a = []
# for i in range(n):
#    number = int(input())
#    a.append(number)
# for i in (a):
#    print(i * i)

n = int(input())
a = []
for i in range(n):
    number = int(input())
    a.append(number)
for i in (a):
    if i % 2 == 0:
        print(i)

