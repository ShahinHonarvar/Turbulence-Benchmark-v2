def if_perfect_num(nums):
    if len(nums) > 68:
        return sum([i for i in range(1, nums[68]) if nums[68] % i == 0]) == nums[68]
    return False