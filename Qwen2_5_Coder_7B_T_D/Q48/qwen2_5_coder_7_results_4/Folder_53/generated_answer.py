def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    total_sum = sum(range(a + 1, b))
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[200:203]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()