def find_second_largest_num(numbers):
    subset = numbers[75:89]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]