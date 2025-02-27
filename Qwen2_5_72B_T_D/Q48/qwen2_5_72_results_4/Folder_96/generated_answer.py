def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    subset = set(numbers[51:200])
    missing_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]