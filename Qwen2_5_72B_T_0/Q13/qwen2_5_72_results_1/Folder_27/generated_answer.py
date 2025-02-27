def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    subset = numbers[66:94]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]