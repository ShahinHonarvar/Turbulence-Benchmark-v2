def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    full_set = set(range(a + 1, b))
    given_set = set(numbers[451:905])
    diff_set = full_set - given_set
    total_sum = sum(diff_set)
    if not diff_set:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()