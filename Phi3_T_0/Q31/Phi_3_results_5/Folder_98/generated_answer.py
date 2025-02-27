def if_perfect_num(nums):
    if len(nums) > 4:
        return sum([i for i in range(1, nums[4]) if nums[4] % i == 0]) == nums[4]
    return False