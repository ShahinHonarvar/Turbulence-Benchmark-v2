def if_perfect_num(nums):
    return sum([i for i in range(1, nums[276]) if nums[276] % i == 0]) == nums[276]