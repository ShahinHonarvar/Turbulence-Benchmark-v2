def if_perfect_num(nums):
    if len(nums) < 18:
        return False
    n = nums[17]
    sum_factors = sum((i for i in range(1, n) if n % i == 0))
    return sum_factors == n