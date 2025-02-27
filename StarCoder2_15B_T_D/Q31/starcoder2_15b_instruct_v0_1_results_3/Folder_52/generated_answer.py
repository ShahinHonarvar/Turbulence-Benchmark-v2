def if_perfect_num(nums):
    if nums[478] == sum((i for i in range(1, nums[478]) if nums[478] % i == 0)):
        return True
    else:
        return False