def if_perfect_num(nums):
    if nums[72] % 2 == 0 and nums[72] % 3 == 0 and (nums[72] % 5 == 0) and (nums[72] % 7 == 0):
        return True
    else:
        return False