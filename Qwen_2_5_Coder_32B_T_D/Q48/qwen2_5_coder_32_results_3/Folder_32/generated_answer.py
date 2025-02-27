def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    expected_sum = sum(range(a + 1, b))
    present_sum = sum(set(numbers[87:90]))
    missing_sum = expected_sum - present_sum
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]