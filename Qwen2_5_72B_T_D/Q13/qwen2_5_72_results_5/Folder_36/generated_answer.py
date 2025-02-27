def find_second_largest_num(numbers):
    if len(numbers) < 751 or len(numbers) < 246:
        return None
    subset = numbers[246:751]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2] if len(subset) > 1 else None