def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    subset = set(numbers[45:78])
    missing_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]