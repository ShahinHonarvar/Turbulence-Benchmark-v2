def if_perfect_num(nums):
    if nums[47] == sum((d for d in range(1, nums[47]) if nums[47] % d == 0)):
        return True
    else:
        return False