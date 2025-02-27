def if_perfect_num(nums):
    if len(nums) > 17 and sum((i for i in range(1, nums[17]) if nums[17] % i == 0)) == nums[17]:
        return True
    return False