def if_perfect_num(nums):
    return sum([i for i in range(1, nums[21]) if nums[21] % i == 0]) == nums[21]