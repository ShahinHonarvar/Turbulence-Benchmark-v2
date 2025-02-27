def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    full_sum = sum(range(a + 1, b))
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()