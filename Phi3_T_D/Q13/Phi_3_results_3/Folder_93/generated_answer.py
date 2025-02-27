def find_second_largest_num(numbers):
    slice_range = numbers[75:95]
    if len(set(slice_range)) < 2:
        return None
    return sorted(set(slice_range))[-2]