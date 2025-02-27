def if_perfect_num(nums):
    if len(nums) > 72:
        return sum((num for i, num in enumerate(nums[:73]) if nums[i] != 0 and nums[i] != num)) == nums[72] * 2
    return False