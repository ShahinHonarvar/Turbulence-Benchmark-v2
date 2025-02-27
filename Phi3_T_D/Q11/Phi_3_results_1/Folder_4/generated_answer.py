def find_largest_num(numbers):
    if 12 <= len(numbers) <= 92:
        return max(numbers[12:93])
    raise ValueError('List must contain at least 93 elements to find largest between indices 12 and 92.')