def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    slice_nums = numbers[6:9]
    if len(slice_nums) < 2:
        return None
    slice_nums.sort()
    return slice_nums[-2]