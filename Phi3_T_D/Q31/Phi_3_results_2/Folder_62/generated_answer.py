def if_perfect_num(nums):
    if len(nums) > 926:
        perfect_sum = sum((i for i in range(1, nums[926]) if nums[926] % i == 0))
        return perfect_sum == nums[926]
    return False