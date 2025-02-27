def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    subset = numbers[:10]
    subset.sort()
    if len(set(subset)) < 2:
        return None
    return subset[-2]