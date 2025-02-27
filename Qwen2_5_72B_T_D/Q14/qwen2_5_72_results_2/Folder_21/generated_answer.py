def find_second_smallest_num(numbers):
    if len(numbers) < 924 or len(numbers) < 661:
        return None
    slice_list = numbers[660:925]
    slice_list.sort()
    if len(slice_list) < 2:
        return None
    return slice_list[1]