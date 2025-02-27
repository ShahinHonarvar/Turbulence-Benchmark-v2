def if_perfect_num(nums):
    if nums[41] == sum((d for d in range(1, nums[41]) if nums[41] % d == 0)):
        return True
    else:
        return False