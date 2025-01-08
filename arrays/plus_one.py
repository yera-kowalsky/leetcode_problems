digits_1 = [1, 2, 3]


def plusOne(digits):
    for i in range(len(digits_1) - 1, -1, -1):
        if digits[i] + 1 != 10:
            digits[i] += 1
            return digits
        digits[i] = 0
        if i == 0:
            return [1] + digits


print(plusOne(digits_1))
