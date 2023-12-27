def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

x = int(input("Введите натуральное число: "))

if is_prime(x):
    print(f"{x} является простым числом.")
else:
    print(f"{x} не является простым числом.")