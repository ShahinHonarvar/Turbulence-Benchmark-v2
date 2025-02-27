def if_perfect_num(nums):
    return sum(nums[27]) == sum([i for i in range(1, nums[27]) if nums[27] % i == 0])