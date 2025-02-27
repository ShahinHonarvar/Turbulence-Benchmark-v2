def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 16:
        return None
    subset = numbers[15:52]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]