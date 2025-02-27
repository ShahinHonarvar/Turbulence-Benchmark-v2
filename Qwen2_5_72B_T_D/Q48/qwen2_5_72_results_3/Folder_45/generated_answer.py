def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    subset = set(numbers[31:200])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]