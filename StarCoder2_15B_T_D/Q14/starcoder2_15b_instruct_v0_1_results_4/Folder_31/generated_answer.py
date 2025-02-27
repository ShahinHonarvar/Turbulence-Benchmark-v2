def find_second_smallest_num(numbers):
    numbers_subset = numbers[29:94]
    sorted_subset = sorted(numbers_subset)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None