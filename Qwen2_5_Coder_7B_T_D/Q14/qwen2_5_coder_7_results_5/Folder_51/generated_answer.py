def find_second_smallest_num(numbers):
    subset = numbers[1:9]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]