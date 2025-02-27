def if_perfect_num(nums):
    if 29 < len(nums):
        return False
    if not isinstance(nums[29], int) or nums[29] < 0:
        return False

    def sum_divisors(n):
        return sum((i for i in range(1, n // 2 + 1) if n % i == 0))
    return n == sum_divisors(nums[29])