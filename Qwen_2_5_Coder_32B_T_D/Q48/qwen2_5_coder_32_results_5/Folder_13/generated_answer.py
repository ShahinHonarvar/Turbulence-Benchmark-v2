def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    full_set = set(range(a + 1, b))
    given_set = set(numbers[47:91])
    diff_set = full_set - given_set
    total_sum = sum(diff_set)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]