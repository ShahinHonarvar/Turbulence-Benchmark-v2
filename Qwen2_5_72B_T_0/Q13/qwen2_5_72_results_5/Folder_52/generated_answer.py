def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    subset = numbers[28:39]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    while subset and subset[-1] == largest:
        subset.remove(largest)
    if not subset:
        return None
    return max(subset)