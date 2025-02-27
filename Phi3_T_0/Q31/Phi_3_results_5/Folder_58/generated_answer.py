def if_perfect_num(nums):
    if len(nums) > 714:
        sum_divisors = sum((i for i in range(1, nums[714]) if nums[714] % i == 0))
        return sum_divisors == nums[714]
    return False