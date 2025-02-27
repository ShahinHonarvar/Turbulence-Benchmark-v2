def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    missing_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(30, 201) if a + 1 <= numbers[i] <= b - 1))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()