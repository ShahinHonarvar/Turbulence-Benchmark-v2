def find_second_largest_num(numbers):
    if len(numbers[29:79]) < 2:
        return None
    sorted_subset = sorted(numbers[29:79], reverse=True)
    return sorted_subset[1]