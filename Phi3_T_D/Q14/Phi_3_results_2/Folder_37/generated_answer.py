def find_second_smallest_num(numbers):
    valid_slice = numbers[5:8]
    if len(valid_slice) < 2:
        return None
    valid_slice.sort()
    return valid_slice[1]