def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    subset = numbers[75:95]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[-2]