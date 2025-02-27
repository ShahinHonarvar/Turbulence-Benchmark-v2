def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    subset = numbers[56:58]
    subset.sort()
    return subset[1] if len(subset) > 1 else None