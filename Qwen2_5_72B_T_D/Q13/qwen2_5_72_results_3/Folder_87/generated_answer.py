def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    subset = numbers[36:47]
    subset.sort()
    if len(set(subset)) == 1:
        return None
    return subset[-2]