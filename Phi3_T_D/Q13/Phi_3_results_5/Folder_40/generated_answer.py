def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    if len(nums) == 2:
        return max(nums[0], nums[1])
    return sorted(nums[:3])[-2]