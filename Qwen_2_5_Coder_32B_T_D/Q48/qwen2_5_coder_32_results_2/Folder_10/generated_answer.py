def return_binary_or_hexa(numbers):
    a, b = (numbers[36], numbers[54])
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((x for x in range(a + 1, b) if x not in numbers[37:54]))
    if actual_sum == expected_sum:
        return ''
    if actual_sum % 2:
        return bin(actual_sum)[2:]
    return hex(actual_sum)[2:].upper()