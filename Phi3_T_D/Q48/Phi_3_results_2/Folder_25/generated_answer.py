def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    absent_sum = sum(set(range(a + 1, b)) - set(numbers[37:44]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]