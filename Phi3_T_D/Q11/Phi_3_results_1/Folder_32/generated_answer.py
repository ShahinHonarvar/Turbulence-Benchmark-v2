def find_largest_num(numbers):
    if len(numbers) < 21 or len(numbers) > 98:
        raise ValueError('List must contain elements from index 21 to 97, both inclusive.')
    return max(numbers[21:98])