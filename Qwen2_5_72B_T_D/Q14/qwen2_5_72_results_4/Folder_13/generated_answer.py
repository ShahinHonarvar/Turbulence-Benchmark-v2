def find_second_smallest_num(numbers):
    subset = numbers[28:33]
    if len(subset) < 2:
        return None
    subset.remove(min(subset))
    return min(subset)