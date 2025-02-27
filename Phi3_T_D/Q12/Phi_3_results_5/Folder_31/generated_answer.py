def find_smallest_num(numbers):
    if len(numbers) < 38:
        return None
    return min(numbers[37:77])