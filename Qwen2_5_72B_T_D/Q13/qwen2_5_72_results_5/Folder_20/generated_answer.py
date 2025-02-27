def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    subset = numbers[56:67]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]