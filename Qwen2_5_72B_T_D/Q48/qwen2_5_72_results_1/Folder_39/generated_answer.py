def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    present = set(numbers[45:91])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]