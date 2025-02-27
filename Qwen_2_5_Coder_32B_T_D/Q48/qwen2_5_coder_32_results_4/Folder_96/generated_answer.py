def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    full_set = set(range(a + 1, b))
    given_set = set(numbers[51:200])
    missing_set = full_set - given_set
    total_sum = sum(missing_set)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()