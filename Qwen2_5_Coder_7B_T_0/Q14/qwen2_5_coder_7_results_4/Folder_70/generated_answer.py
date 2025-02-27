def find_second_smallest_num(numbers):
    subset = numbers[35:50]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]