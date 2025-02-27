def find_second_smallest_num(numbers):
    subset = numbers[12:93]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]