def if_perfect_num(nums):
    if len(nums) > 63 and nums[63] == sum((divisor for divisor in range(1, nums[63]) if nums[63] % divisor == 0)):
        return True
    return False