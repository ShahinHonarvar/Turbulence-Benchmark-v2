def if_perfect_num(nums):
    return sum((nums[83] // i for i in range(1, int(nums[83] ** 0.5) + 1) if nums[83] % i == 0)) == nums[83] and nums[83] != 1