def if_perfect_num(nums):
    return sum([i for i in range(1, nums[845]) if nums[845] % i == 0]) == nums[845] and nums[845] != 1