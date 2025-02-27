def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    subset = numbers[28:39]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]