def find_second_smallest_num(numbers):
    if not 51 >= len(numbers) >= 30:
        return None
    subset = numbers[29:52]
    subset.sort()
    return subset[1] if len(subset) > 1 else None