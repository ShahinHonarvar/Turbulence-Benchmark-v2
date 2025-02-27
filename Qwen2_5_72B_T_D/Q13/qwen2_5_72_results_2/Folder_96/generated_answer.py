def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 16:
        return None
    subset = numbers[15:52]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]