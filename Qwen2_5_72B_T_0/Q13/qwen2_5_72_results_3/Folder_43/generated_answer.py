def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    subset = numbers[68:87]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]