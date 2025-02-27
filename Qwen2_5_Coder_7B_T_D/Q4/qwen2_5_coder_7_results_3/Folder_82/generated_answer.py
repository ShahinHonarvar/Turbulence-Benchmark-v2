def all_pos_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 20 and i < 200 and (num > 0)]