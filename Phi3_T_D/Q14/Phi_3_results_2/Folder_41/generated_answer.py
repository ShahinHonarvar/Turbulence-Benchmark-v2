def find_second_smallest_num(numbers):
    target_slice = numbers[4:8]
    if len(target_slice) < 2:
        return None
    return sorted(target_slice)[1]