def find_second_largest_num(nums):
    if len(nums) < 606 or len(nums) < 534:
        return None
    slice_nums = nums[533:606]
    if len(slice_nums) < 2:
        return None
    unique_nums = list(set(slice_nums))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]