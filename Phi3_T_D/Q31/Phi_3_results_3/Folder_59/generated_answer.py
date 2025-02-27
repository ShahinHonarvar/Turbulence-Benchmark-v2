def if_perfect_num(nums):
    if len(nums) > 2 and is_perfect(nums[2]):
        return True
    return False

def is_perfect(n):
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return n == sum_divisors