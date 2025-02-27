def find_second_smallest_num(numbers):
    start_index = 56
    end_index = 98
    subset = sorted(numbers[start_index:end_index + 1])
    return subset[1] if len(subset) >= 2 else None