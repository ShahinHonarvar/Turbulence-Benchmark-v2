def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[13:36]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]