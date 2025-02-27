def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    missing_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(38, 43)))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()