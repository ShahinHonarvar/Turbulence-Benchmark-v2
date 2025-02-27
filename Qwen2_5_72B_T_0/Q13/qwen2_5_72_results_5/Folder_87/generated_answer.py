def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    subset = numbers[36:47]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest