def find_largest_num(numbers):
    if len(numbers) < 94:
        raise ValueError('List must contain at least 94 elements')
    return max(numbers[66:94])