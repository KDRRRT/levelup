# a = input().split()
# lst = []
# for i in range(len(a)):
#    lst.append(int(a[i]))


# def change(lst):
#    lst[0], lst[-1] = lst[-1], lst[0]
#    print(lst)


# change(lst)


# a = input().split()
# lst = []
# for i in range(len(a)):
#    lst.append(int(a[i]))
# c = 0
# for i in range(1, len(lst) - 1):
#    if lst[i - 1] < lst[i] > lst[i + 1]:
#        c += 1

# print(c)

a = input().split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))
lst.sort()
b = 0
saw = []
for i in lst:
    if i not in saw:
        b += 1
        saw.append(i)
print(b)

# b = 1                          ЭТА НЕПРАВИЛЬНЫЙ ВАРИАНТ
# for i in range(len(lst) - 1):
#     if lst[i] is not lst[i + 1]:
#         b += 1
# print(b)
