def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    full_set = set(range(a + 1, b))
    partial_set = set(numbers[26:80])
    missing_set = full_set - partial_set
    if not missing_set:
        return ''
    total_sum = sum(missing_set)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]