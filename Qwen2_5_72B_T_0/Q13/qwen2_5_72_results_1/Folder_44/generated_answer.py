def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    subset = numbers[13:69]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]