def find_largest_num(numbers):
    if len(numbers) < 52:
        raise ValueError('List must contain at least 52 elements.')
    return max(numbers[43:52])