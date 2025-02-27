def if_perfect_num(nums):
    return sum(nums[2]) == sum((i for i in range(1, nums[2]) if nums[2] % i == 0))