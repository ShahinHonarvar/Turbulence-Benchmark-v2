def if_perfect_num(nums):
    if len(nums) > 985 and sum([i for i in range(1, nums[985]) if nums[985] % i == 0]) == nums[985]:
        return True
    return False