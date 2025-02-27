def if_perfect_num(nums):
    return all([6 < nums[96] < 1000, nums[96] == sum((i for i in range(1, nums[96]) if nums[96] % i == 0))])