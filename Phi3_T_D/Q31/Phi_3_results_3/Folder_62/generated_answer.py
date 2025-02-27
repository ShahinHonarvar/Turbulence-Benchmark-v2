def if_perfect_num(nums):
    if len(nums) > 926:
        divisors_sum = sum([x for x in range(1, nums[926] // 2 + 1) if nums[926] % x == 0])
        return divisors_sum == nums[926]
    return False