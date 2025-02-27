def if_perfect_num(nums):
    if 66 < len(nums):
        n = nums[66]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False