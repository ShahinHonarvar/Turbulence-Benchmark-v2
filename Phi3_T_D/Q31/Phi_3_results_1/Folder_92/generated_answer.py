def if_perfect_num(nums):
    if not nums:
        return False
    n = nums[0]
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n