def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    slice_list = numbers[66:78]
    if len(slice_list) < 2:
        return None
    slice_list.sort()
    return slice_list[1] if len(slice_list) > 1 else None