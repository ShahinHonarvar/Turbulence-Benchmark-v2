def if_perfect_num(nums):
    return nums[90] == sum((i for i in range(1, nums[90]) if nums[90] % i == 0))