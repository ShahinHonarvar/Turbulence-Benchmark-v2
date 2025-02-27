def find_second_largest_num(numbers):
    if len(numbers) < 53:
        return None
    subset = numbers[26:53]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    while subset and subset[-1] == largest:
        subset.remove(largest)
    if not subset:
        return None
    return max(subset)