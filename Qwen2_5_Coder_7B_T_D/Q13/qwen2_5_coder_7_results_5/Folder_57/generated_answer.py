def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    subset = numbers[27:56]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[-2]