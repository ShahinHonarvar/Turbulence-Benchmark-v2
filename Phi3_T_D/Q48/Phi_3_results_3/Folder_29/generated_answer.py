def return_binary_or_hexa(numbers):
    if 70 > len(numbers) or 98 < len(numbers):
        return ''
    missing_sum = sum(set(range(numbers[70] + 1, numbers[98])) - set(numbers[70:98]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]