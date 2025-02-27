def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[51]
    start, end = (a + 1, b - 1)
    missing_sum = sum((i for i in range(start, end + 1) if i not in numbers[start:end + 1]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()