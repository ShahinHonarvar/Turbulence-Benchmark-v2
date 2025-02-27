def find_second_largest_num(numbers):
    subset = numbers[30:88]
    if len(subset) < 2:
        return None
    subset = sorted(subset, reverse=True)
    return subset[1]