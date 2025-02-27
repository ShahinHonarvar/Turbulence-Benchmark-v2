def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    subset = sorted(numbers[62:64])
    return subset[1] if len(subset) > 1 else None