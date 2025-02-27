def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    missing_sum_set = set(range(a + 1, b)) - set(numbers[68:99 + 1])
    if not missing_sum_set:
        return ''
    missing_sum = sum(missing_sum_set)
    if missing_sum % 2 == 0:
        return hex(missing_sum).upper().lstrip('0').lstrip('H')
    else:
        return bin(missing_sum).lstrip('0b')