def find_largest_num(nums):
    return max(nums[36:46]) if len(nums) > 46 else max(nums[36:len(nums)])