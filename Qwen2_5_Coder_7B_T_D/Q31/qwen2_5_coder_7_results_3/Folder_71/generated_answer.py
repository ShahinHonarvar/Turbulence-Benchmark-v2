def if_perfect_num(nums):
    return sum([i for i in range(1, nums[78]) if nums[78] % i == 0]) == nums[78] if len(nums) > 78 else False