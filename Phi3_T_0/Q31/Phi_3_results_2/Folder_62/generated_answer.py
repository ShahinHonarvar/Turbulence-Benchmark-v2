def if_perfect_num(nums):
    if len(nums) > 926:
        sum_divisors = sum((i for i in range(1, nums[926]) if nums[926] % i == 0))
        return sum_divisors == nums[926]
    return False