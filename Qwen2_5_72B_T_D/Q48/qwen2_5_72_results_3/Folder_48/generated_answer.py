def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[934:996]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]