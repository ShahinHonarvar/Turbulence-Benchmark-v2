def all_pos_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 91 <= i <= 99 and num > 0]