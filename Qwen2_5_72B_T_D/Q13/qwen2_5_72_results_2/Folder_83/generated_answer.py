def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    subset = numbers[90:91]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]