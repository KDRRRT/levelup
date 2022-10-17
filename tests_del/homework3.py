# a = input().split()
# lst = []
# for i in range(len(a)):
#     lst.append(int(a[i]))
# print(lst)
# n = int(input())
# my_list = []
# for i in range(n):
#     number = int(input())
#     my_list.append(number)
# print(my_list)


def read_input():
    a = float(input())
    b = float(input())
    c = input()
    return a, b, c


def calculate(a, b, c):
    if c == "+":
        print(f" {a} {c} {b} = {(a + b)}")
    elif c == "-":
        print(f" {a} {c} {b} = {(a - b)}")
    elif c == "*":
        print(f" {a} {c} {b} = {(a * b)}")
    elif c == "/" and b > 0:
        print(f" {a} {c} {b} = {(a / b)}")
    elif c == "/" and b == 0:
        print("На ноль делить нельзя")

    else:
        print("Операция невозможна")


a, b, c = read_input()
calculate(a, b, c)



# user = f" {a} {c} {b} = {d}" #это схема для того, чтобы написать решение

