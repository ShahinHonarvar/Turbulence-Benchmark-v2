def find_smallest_num(numbers):
    return min(numbers[:4]) if len(numbers) >= 4 else min(numbers)