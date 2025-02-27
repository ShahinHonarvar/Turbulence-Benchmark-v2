def find_second_smallest_num(numbers):
    target_slice = numbers[74:95 + 1]
    if len(target_slice) < 2:
        return None
    sorted_slice = sorted(target_slice)
    return sorted_slice[1] if len(sorted_slice) > 1 else None