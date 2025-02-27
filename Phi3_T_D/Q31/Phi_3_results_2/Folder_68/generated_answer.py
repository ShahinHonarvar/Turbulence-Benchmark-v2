def if_perfect_num(nums):
    perfect = sum((i for i in range(1, nums[3]) if nums[3] % i == 0)) == nums[3]
    return perfect