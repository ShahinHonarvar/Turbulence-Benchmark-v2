def find_second_largest_num(numbers):
    subset = numbers[33:37]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)