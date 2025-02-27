def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[:9]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    while subset and subset[0] == largest:
        subset.remove(largest)
    if not subset:
        return None
    return max(subset)