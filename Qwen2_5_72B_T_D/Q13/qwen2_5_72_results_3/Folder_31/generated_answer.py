def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    subset = numbers[75:89]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]