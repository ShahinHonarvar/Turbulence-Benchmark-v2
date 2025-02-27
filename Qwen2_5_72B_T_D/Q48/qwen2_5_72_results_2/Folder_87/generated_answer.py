def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[21:43]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]