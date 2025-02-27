def is_perfect_num(nums):
    if len(nums) <= 41:
        return False
    n = nums[41]
    sum_divisors = sum([x for x in range(1, n // 2 + 1) if n % x == 0])
    return sum_divisors == n