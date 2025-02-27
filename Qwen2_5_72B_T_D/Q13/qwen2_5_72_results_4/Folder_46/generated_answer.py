def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    subset = numbers[30:88]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]