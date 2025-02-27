def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[4:5]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest