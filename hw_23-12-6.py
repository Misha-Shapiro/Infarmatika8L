def is_same_color(x1, y1, x2, y2):
    return (x1 + y1) % 2 == (x2 + y2) % 2
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))
if is_same_color(x1, y1, x2, y2):
    print("Клетки одного цвета")
else:
    print("Клетки разного цвета")