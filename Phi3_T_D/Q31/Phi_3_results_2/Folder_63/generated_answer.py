def if_perfect_num(nums):
    if len(nums) > 57 and sum((i for i in range(1, nums[57] // 2 + 1) if nums[57] % i == 0)) == nums[57]:
        return True
    return False