def find_second_largest_num(numbers):
    if len(numbers) < 36:
        return None
    subset = numbers[32:36]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]