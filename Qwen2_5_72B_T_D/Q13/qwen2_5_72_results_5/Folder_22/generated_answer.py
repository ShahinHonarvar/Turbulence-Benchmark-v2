def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 41:
        return None
    subset = numbers[40:201]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    while subset and largest == max(subset):
        subset.remove(max(subset))
    if subset:
        return max(subset)
    return None