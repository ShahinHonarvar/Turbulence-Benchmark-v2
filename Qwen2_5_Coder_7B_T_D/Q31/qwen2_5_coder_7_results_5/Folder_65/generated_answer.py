def if_perfect_num(nums):
    return nums[35] == sum((i for i in range(1, nums[35]) if nums[35] % i == 0))