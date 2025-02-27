def find_second_largest_num(numbers):
    if len(numbers) < 65 or len(numbers) > 65:
        return None
    subset = numbers[14:65]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2] if len(subset) > 1 else None