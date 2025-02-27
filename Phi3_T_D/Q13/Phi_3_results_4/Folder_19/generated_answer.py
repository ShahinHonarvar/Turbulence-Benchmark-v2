def find_second_largest_num(nums):
    if len(nums) < 6 or (len(nums) < 3 or nums[3] == nums[4] == nums[5]):
        return None
    slice_of_nums = sorted(nums[3:6], reverse=True)
    return slice_of_nums[1]