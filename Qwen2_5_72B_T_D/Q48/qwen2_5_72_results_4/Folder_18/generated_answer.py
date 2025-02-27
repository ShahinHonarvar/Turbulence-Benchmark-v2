def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    present = set(numbers[56:91])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]