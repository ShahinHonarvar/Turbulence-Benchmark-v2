def if_perfect_num(nums):
    if len(nums) > 56 and sum((i for i in range(1, nums[56]) if nums[56] % i == 0)) == nums[56]:
        return True
    else:
        return False