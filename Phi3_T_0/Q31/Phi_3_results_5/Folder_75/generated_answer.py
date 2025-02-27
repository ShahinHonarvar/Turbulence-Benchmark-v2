def if_perfect_num(nums):
    if len(nums) > 80:
        return sum([i for i in range(1, nums[80]) if nums[80] % i == 0]) == nums[80]
    return False