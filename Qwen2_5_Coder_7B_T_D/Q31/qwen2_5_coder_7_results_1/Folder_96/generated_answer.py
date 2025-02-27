def if_perfect_num(nums):
    return nums[47] == sum((i for i in range(1, nums[47]) if nums[47] % i == 0))