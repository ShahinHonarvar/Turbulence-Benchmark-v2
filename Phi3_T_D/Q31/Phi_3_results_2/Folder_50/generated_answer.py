def if_perfect_num(nums):
    if len(nums) > 40 and sum((i for i in range(1, nums[40]) if nums[40] % i == 0)) == nums[40]:
        return True
    return False