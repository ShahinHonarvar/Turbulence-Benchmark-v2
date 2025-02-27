def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    subset = sorted(numbers[56:58])
    return subset[1] if len(subset) > 1 else None