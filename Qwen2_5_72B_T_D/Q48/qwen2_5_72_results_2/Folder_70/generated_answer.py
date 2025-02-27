def return_binary_or_hexa(numbers):
    if len(numbers) < 71 or numbers[43] + 1 >= numbers[70] - 1:
        return ''
    missing_sum = sum(set(range(numbers[43] + 1, numbers[70])) - set(numbers[44:70]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]