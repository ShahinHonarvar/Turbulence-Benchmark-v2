def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    missing_sum = sum(range(a + 1, b)) - sum(set(numbers[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()