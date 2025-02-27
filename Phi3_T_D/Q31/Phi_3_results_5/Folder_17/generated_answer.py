def if_perfect_num(nums):
    if 632 < len(nums):
        n = nums[632]
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    return False