def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    subset = numbers[56:67]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest