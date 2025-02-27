def find_second_largest_num(numbers):
    if len(numbers) < 774:
        return None
    subset = numbers[667:775]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]