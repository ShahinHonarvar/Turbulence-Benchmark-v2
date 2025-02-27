def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[39:44]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]