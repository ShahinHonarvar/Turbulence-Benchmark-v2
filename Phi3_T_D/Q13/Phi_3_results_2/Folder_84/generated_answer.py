def find_second_largest_num(numbers):
    target_slice = numbers[43:87]
    unique_target_slice = set(target_slice)
    if len(unique_target_slice) < 2:
        return None
    return sorted(unique_target_slice)[-2]