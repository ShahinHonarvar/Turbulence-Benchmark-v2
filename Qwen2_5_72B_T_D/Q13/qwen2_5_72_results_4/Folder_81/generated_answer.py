def find_second_largest_num(numbers):
    if len(numbers) < 101 or len(numbers) < 11:
        return None
    subset = numbers[10:101]
    subset.sort()
    return subset[-2] if len(subset) > 1 else None