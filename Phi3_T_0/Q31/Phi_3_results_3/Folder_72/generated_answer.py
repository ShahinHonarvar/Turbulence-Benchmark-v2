def if_perfect_num(nums):
    if len(nums) > 16 and sum((i for i in range(1, nums[16]) if nums[16] % i == 0)) == nums[16]:
        return True
    return False