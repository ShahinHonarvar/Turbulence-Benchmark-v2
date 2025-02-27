def if_perfect_num(nums):
    if len(nums) > 13:
        return sum([i for i in range(1, nums[13]) if nums[13] % i == 0]) == nums[13]
    return False