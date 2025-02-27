def find_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    return min(numbers[:6])