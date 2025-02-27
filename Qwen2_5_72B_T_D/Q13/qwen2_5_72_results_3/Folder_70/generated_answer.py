def find_second_largest_num(numbers):
    subset = numbers[28:33]
    if len(subset) < 5:
        return None
    subset.sort()
    return subset[-2] if len(subset) > 1 else None