def if_perfect_num(nums):
    if len(nums) > 828:
        divisor_sum = sum((i for i in range(1, nums[828]) if nums[828] % i == 0))
        return divisor_sum == nums[828]
    return False