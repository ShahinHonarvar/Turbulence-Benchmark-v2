def find_largest_num(numbers):
    if len(numbers) < 775:
        raise ValueError('List must contain at least 775 elements')
    return max(numbers[667:775])