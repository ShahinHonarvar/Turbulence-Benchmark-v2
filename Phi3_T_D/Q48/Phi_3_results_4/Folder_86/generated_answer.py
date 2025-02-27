def return_binary_or_hexa(numbers):
    if len(numbers) < 32:
        return ''
    missing_sum = sum((i for i in range(numbers[19] + 1, numbers[32]) if i not in numbers[19:32]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return '{:x}'.format(missing_sum)