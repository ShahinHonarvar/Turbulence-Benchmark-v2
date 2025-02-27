def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[:9]
    subset.sort()
    return subset[-2]