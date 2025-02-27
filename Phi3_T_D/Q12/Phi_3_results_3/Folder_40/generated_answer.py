def find_smallest_num(numbers):
    if not numbers or len(numbers) < 2:
        return None
    return min(numbers[0], numbers[1])