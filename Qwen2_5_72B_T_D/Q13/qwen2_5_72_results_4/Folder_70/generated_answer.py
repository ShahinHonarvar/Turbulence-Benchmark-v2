def find_second_largest_num(numbers):
    if len(numbers) < 33:
        return None
    slice_list = numbers[28:33]
    if len(slice_list) < 2:
        return None
    unique_nums = list(set(slice_list))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]