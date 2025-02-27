def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    full_set = set(range(a + 1, b))
    present_set = set(numbers[451:905])
    missing_sum = sum(full_set - present_set)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]