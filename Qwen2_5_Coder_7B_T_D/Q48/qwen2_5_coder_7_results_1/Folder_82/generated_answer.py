def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    total_sum = sum(range(a + 1, b))
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()