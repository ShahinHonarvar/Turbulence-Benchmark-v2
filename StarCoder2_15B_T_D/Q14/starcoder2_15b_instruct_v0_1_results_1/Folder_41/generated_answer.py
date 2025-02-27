def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 6 or nums[4] == nums[5]:
        return None
    return nums[5]