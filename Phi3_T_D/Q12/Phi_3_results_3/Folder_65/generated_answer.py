def find_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    return min(numbers[12:93])