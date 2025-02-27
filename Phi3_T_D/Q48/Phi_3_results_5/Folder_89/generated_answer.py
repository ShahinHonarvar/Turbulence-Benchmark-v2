def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    absent_sum = sum(set(range(a + 1, b)).difference(numbers[55:85]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]