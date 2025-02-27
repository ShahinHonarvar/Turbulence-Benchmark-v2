def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    full_set = set(range(a + 1, b))
    existing_set = set(numbers[87:99])
    missing_sum = sum(full_set - existing_set)
    if missing_sum:
        if missing_sum % 2:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:]
    return ''