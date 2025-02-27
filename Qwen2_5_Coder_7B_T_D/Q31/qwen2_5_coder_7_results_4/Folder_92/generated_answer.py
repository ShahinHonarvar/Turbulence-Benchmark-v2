def if_perfect_num(nums):
    if sum(nums[1:]) == nums[0]:
        return True
    else:
        return False