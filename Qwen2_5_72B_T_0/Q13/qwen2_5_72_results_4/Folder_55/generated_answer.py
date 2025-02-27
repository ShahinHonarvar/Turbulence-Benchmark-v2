def find_second_largest_num(numbers):
    if len(numbers) < 11:
        return None
    subset = numbers[:11]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]