def if_perfect_num(nums):
    if len(nums) > 10:
        return sum([i for i in range(1, nums[10]) if nums[10] % i == 0]) == nums[10]
    return False