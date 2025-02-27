def find_second_smallest_num(numbers):
    subset = numbers[29:52]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1] if len(subset) > 1 else None