def if_perfect_num(nums):
    if len(nums) <= 41:
        return False
    n = nums[41]
    divisors_sum = sum([x for x in range(1, n) if n % x == 0])
    return divisors_sum == n