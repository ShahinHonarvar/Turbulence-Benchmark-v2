def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    present_numbers = set(numbers[14:70])
    missing_sum = sum(set(range(a + 1, b)) - present_numbers)
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]