def if_perfect_num(nums):
    if len(nums) > 3 and sum((i for i in range(1, nums[3]) if nums[3] % i == 0)) == nums[3]:
        return True
    return False