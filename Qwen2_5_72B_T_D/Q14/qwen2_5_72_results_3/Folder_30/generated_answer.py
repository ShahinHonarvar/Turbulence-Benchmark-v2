def find_second_smallest_num(numbers):
    if len(numbers) < 53:
        return None
    subset = numbers[26:53]
    subset.sort()
    return subset[1] if len(subset) > 1 else None