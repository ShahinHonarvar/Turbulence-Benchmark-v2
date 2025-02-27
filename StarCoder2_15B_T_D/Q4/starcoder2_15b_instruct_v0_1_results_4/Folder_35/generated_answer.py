def all_pos_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 10 <= i < 79 and num > 0]