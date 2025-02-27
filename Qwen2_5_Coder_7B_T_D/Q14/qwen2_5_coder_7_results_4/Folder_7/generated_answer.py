def find_second_smallest_num(numbers):
    subset = numbers[686:988]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]