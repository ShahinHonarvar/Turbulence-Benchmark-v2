def find_second_largest_num(numbers):
    if len(numbers) < 24:
        return None
    subset = numbers[23:24]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    return max(subset)