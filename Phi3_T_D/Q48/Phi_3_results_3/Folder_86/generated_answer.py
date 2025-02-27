def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    missing_sum = sum(range(a + 1, b)) - sum(numbers[19:32])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]