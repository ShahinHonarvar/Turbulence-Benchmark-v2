def find_second_largest_num(numbers):
    start, end = (12, 93)
    subset = numbers[start:end]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    return max(subset)