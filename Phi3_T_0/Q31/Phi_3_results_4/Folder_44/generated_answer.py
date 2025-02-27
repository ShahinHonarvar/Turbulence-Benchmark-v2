def if_perfect_num(nums):
    if len(nums) > 828:
        sum_divisors = sum((i for i in range(1, nums[828]) if nums[828] % i == 0))
        return sum_divisors == nums[828]
    return False