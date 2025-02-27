def find_second_largest_num(numbers):
    subset = numbers[75:95]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]