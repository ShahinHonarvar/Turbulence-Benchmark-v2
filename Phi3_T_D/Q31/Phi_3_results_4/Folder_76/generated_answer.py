def if_perfect_num(nums):
    if len(nums) > 537 and sum((n for i in range(1, nums[537]) if nums[537] % i == 0)) == nums[537]:
        return True
    return False