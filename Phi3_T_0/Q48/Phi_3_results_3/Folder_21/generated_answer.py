def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[15:58]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]