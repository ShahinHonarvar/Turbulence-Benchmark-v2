def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    return nums[0] if nums[0] > nums[1] else nums[1]