def if_perfect_num(nums):
    if 263 < len(nums):
        n = nums[263]
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    return False