def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    full_set = set(range(a + 1, b))
    numbers_set = set(numbers[1:9])
    missing_numbers_sum = sum(full_set - numbers_set)
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]