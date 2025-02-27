def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    missing_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(18, 88)))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()