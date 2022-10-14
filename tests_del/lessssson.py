# def sort(lst):
#     if sorted(lst) == lst:
#         return True
#     else:
#         return False
#
#
# a = input().split()
# lst = []
# for i in range(len(a)):
#     lst.append(int(a[i]))
# sort(lst)


def count_range(lst, min_n, max_n):
    final = []

    for i in range(len(lst)):
        if i in range(min_n, max_n - 1):
            final.append(lst[i])

    return final


a = input().split()
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))
min_n = int(input())
max_n = int(input())

b_res = count_range(lst, min_n, max_n)
print(b_res)