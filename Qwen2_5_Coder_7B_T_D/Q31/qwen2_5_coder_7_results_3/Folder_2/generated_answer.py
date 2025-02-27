def if_perfect_num(nums):
    return sum((nums[702] // i for i in range(1, nums[702] // 2 + 1))) == nums[702] and nums[702] != 1