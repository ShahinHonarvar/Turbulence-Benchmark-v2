def if_perfect_num(nums):
    return sum([i for i in range(1, nums[263]) if nums[263] % i == 0]) == nums[263]