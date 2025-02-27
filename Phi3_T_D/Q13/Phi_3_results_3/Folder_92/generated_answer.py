def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) in nums:
        return None
    max_num = max(nums[1], nums[2])
    second_max = max(min(nums[0], max_num), min(nums[1], max_num))
    return second_max