def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    slice_nums = numbers[35:50]
    if len(slice_nums) < 2:
        return None
    slice_nums.sort(reverse=True)
    return slice_nums[1] if len(slice_nums) > 1 else None