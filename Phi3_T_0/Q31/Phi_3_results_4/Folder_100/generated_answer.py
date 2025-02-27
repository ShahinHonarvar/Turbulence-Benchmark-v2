def if_perfect_num(nums):
    if len(nums) > 99:
        return sum([i for i in range(1, nums[99]) if nums[99] % i == 0]) == nums[99]
    return False