def find_smallest_num(numbers):
    if len(numbers) < 924:
        raise ValueError('List must have at least 924 elements')
    return min(numbers[660:924])