def find_second_largest_num(numbers):
    subset = numbers[5:8]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]