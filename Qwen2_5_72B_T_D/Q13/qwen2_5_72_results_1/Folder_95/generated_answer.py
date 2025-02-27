def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    slice_list = numbers[82:87]
    slice_list.sort()
    if len(slice_list) < 2:
        return None
    return slice_list[-2]