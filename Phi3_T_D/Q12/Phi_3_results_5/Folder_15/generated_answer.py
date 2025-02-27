def find_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    return min(numbers[:3])