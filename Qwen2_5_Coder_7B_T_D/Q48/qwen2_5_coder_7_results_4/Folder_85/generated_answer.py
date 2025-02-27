def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    missing_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(2, 9)))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()