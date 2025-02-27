def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    full_set = set(range(a + 1, b))
    numbers_set = set(numbers[61:200])
    missing_sum = sum(full_set - numbers_set)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]