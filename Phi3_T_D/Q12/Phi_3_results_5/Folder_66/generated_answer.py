def find_smallest_num(numbers):
    if len(numbers) < 79:
        raise ValueError('List must have at least 79 elements.')
    return min(numbers[62:79])