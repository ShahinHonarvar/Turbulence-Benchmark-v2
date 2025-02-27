def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[1:6]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]