def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    missing_sum = sum(range(a + 1, b)) - sum(numbers[69:99])
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]