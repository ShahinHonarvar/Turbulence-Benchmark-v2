def find_second_smallest_num(numbers):
    if 8 < len(numbers):
        numbers = numbers[:9]
    if len(numbers) < 2:
        return None
    min_val = min(numbers)
    numbers.remove(min_val)
    return min(numbers)