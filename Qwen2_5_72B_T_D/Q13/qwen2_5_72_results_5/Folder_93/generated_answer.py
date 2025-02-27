def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    subset = numbers[75:95]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest