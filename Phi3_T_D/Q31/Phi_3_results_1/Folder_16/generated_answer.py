def if_perfect_num(nums):
    return sum((i for i in range(1, nums[162] // 2 + 1) if nums[162] % i == 0)) == nums[162]