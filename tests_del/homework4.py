import matplotlib.pyplot as plt

# def roots(a, b, c):
a = int(input())
b = int(input())
c = int(input())
if __name__ == "__main__":
    dis = b ** 2 - 4 * a * c
    if dis < 0:
        print("Корней нет")
    elif dis == 0:
        x = -b / (2 * a)
        print(x)
    else:
        x1 = (-b + dis ** 0.5) / (2 * a)
        x2 = (-b - dis ** 0.5) / (2 * a)
        print(x1)
        print(x2)


x1 = [1, 2, 3, 4, 5]
x2 = [1, 2, 3, 4, 5]
plt.plot(x1, x2)
plt.show()
# roots(a, b, c)
