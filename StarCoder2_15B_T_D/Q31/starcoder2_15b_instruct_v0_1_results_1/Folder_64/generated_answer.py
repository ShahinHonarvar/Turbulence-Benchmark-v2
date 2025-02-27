def if_perfect_num(nums):
    if nums[1] == sum((n for n in range(1, nums[1]) if nums[1] % n == 0)):
        return True
    return False