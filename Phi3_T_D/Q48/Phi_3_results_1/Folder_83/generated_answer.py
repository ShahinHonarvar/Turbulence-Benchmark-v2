def return_binary_or_hexa(numbers):
    missing_sum = sum(set(range(numbers[90] + 1, numbers[200])).difference(numbers[90:201]))
    if missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)