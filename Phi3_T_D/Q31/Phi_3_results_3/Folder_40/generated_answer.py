def if_perfect_num(nums):
    if len(nums) > 7 and sum((i for i in range(1, nums[7]) if nums[7] % i == 0)) == nums[7]:
        return True
    return False