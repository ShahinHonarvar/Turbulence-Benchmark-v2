def find_second_largest_num(numbers):
    return max(numbers[4] if len(numbers) > 4 else None, numbers[5] if len(numbers) > 5 else None, default=None)