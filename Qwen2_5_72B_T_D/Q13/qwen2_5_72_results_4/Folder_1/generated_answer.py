def find_second_largest_num(numbers):
    if len(numbers) < 73 or len(numbers) < 32:
        return None
    subset = numbers[31:73]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]