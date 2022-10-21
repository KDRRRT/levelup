import json

a = input("Сколько см в 1 дм?")
b = input("Сумма углов треугольника?")
c = input("Какой результат дает возведение числа в степень 0?")
# data2 = {"q1": a, "q2": b, "q3": c}
# with open('json_data2.json', "w", encoding="utf-8") as json_file:
#     json.dump(data2, json_file)

# ВТОРАЯ ЗАДАЧКА
with open('json_data2.json') as json_file:
    data = json.load(json_file)
score = 0
if data["q1"] == "10":
    score += 1
if data["q2"] == "180":
    score += 1
if data["q3"] == "1":
    score += 1
print(score)








