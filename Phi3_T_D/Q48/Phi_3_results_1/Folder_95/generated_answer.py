def return_binary_or_hexa(numbers):
    missing_sum = sum(set(range(numbers[32] + 1, numbers[99])) - set(numbers[32:99]))
    if missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)