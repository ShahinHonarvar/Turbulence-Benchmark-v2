def return_binary_or_hexa(numbers):
    a = numbers[18] + 1
    b = numbers[60] - 1
    missing_sum = sum(set(range(a, b + 1)).difference(numbers[18:61]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]