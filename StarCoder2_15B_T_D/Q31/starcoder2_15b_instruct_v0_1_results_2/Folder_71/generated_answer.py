def if_perfect_num(nums):
    if nums[78] == sum((d for d in range(1, nums[78]) if nums[78] % d == 0)):
        return True
    else:
        return False