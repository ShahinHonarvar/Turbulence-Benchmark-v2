def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None
    subset = numbers[30:49]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    while subset and subset[-1] == largest:
        subset.pop()
    return max(subset) if subset else None