def if_perfect_num(nums):
    if len(nums) > 67:
        return sum([i for i in range(1, nums[67]) if nums[67] % i == 0]) == nums[67]
    return False