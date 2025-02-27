def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    subset = numbers[62:93]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest