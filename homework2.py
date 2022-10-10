# a = input().split()
# lst = []
# for i in range(len(a)):
#     lst.append(int(a[i]))
#
#
# lst.reverse()
# print(lst)


a = input().split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))

print(max(lst)) #максимальное число
print(min(lst))  #минимальное число
nlst = sorted(lst)
print(nlst) #сортировка списка


sred = sum(lst) / len(lst)
print(sred) #среднее арифметическое




