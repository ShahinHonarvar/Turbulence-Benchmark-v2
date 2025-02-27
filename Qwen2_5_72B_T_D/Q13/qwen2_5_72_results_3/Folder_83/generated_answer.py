def find_second_largest_num(numbers):
    if len(numbers) <= 90:
        return None
    slice_list = numbers[90:91]
    if len(slice_list) < 2:
        return None
    slice_list.sort()
    return slice_list[-2]