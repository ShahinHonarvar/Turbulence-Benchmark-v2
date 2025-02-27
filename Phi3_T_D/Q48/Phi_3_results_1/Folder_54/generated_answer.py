def return_binary_or_hexa(numbers):
    a = numbers[35] + 1
    b = numbers[64] - 1
    missing_sum = sum((x for x in range(a, b + 1) if x not in numbers[35:65]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]