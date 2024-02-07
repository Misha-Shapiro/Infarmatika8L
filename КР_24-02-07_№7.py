def get_digit_sum(n):
    return sum(int(digit) for digit in str(n))

x = [123, 456, 789, 111, 222]
m = max(get_digit_sum(num) for num in x)

r = [num for num in x if get_digit_sum(num) == m]

print("Числа с максимальной суммой цифр:", r)