def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[:5]
    subset.sort()
    if len(set(subset)) < 2:
        return None
    return subset[-2]