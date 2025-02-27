def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    subset = numbers[66:78]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1] if len(subset) > 1 else None