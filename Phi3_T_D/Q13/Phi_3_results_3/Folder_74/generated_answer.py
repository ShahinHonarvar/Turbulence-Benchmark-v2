def find_second_largest_num(nums):
    slice_of_nums = nums[17:79]
    if len(slice_of_nums) < 2:
        return None
    slice_of_nums.remove(max(slice_of_nums))
    return max(slice_of_nums)