def find_smallest_num(numbers):
    if len(numbers) < 65:
        raise ValueError('List should contain at least 65 elements')
    return min(numbers[64:67])